from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class TravelRequest(models.Model):
    _name = 'employee.travel'
    _description = 'Employee Travel Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', required=True, copy=False, default='New')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, readonly=True, default=lambda self: self._get_current_employee())
    subject = fields.Char(string='Objet / Mission', required=True)
    order_document = fields.Binary(string='Ordre de mission')
    order_filename = fields.Char(string='Order filename')
    date_from = fields.Date(string='Date de début', required=True)
    date_to = fields.Date(string='Date de fin', required=True)
    destination_country_id = fields.Many2one('res.country', string='Pays de destination')
    destination_city_id = fields.Many2one('travel.city', string='Ville de destination', 
                                          domain="[('country_id', '=', destination_country_id)]")
    destination_city = fields.Char(string='Ville (texte libre)', help="Utilisé si la ville n'est pas dans la liste")
    distance_km = fields.Float(string='Distance estimée (Km)', digits=(12, 2))
    transport_mode = fields.Selection([
        ('train', 'Train'),
        ('bus', 'Autocar'),
        ('plane', 'Avion'),
        ('vehicle', 'Véhicule de service')
    ], string='Mode de transport', required=True, default='train')
    vehicle_id = fields.Many2one('employee.travel.vehicle', string='Véhicule de service')
    plane_class = fields.Selection([('economy', 'Economique'), ('business', 'Business')], string='Classe avion')
    days = fields.Integer(string='Nombre de jours', compute='_compute_days', store=True)
    amount = fields.Monetary(string='Montant estimé', currency_field='company_currency_id', compute='_compute_amount', store=True)
    company_currency_id = fields.Many2one('res.currency', string='Currency', related='employee_id.company_id.currency_id', readonly=True)
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('submitted', 'Soumise'),
        ('in_progress', 'En cours de validation'),
        ('approved', 'Approuvée par Manager'),
        ('daf_review', 'En cours DAF'),
        ('daf_approved', 'Validée DAF'),
        ('done', 'Terminée'),
        ('refused', 'Refusée'),
        ('cancelled', 'Annulée'),
    ], string='État', default='draft', tracking=True)
    
    # Workflow fields
    submitted_by = fields.Many2one('res.users', string='Soumise par', readonly=True)
    submitted_date = fields.Datetime(string='Date de soumission', readonly=True)
    approved_by = fields.Many2one('res.users', string='Approuvée par', readonly=True)
    approved_date = fields.Datetime(string='Date d\'approbation', readonly=True)
    daf_user_id = fields.Many2one('res.users', string='Traitée par DAF', readonly=True)
    daf_date = fields.Datetime(string='Date traitement DAF', readonly=True)
    refusal_reason = fields.Text(string='Motif de refus')
    
    # Computed fields for security
    can_submit = fields.Boolean(compute='_compute_user_rights')
    can_approve = fields.Boolean(compute='_compute_user_rights')
    can_daf_validate = fields.Boolean(compute='_compute_user_rights')
    can_cancel = fields.Boolean(compute='_compute_user_rights')

    _sql_constraints = [
        ('date_check', 'CHECK(date_from <= date_to)', 'La date de début doit être antérieure ou égale à la date de fin.')
    ]

    @api.model
    def default_get(self, fields_list):
        """Set default values when creating a new travel request"""
        res = super().default_get(fields_list)
        
        # Auto-fill employee information for current user (cannot be changed)
        employee_id = self._get_current_employee()
        if employee_id:
            res['employee_id'] = employee_id
            
            # Auto-fill company country as default destination country
            try:
                employee = self.env['hr.employee'].browse(employee_id)
                if (employee.company_id and 
                    employee.company_id.partner_id and 
                    employee.company_id.partner_id.country_id):
                    res['destination_country_id'] = employee.company_id.partner_id.country_id.id
            except:
                pass
        
        return res

    def _get_current_employee(self):
        """Get employee record for current user"""
        current_user = self.env.user
        if current_user:
            try:
                # Find employee record for current user
                employee = self.env['hr.employee'].search([
                    ('user_id', '=', current_user.id),
                    ('active', '=', True)
                ], limit=1)
                
                # If no active employee found, try any employee
                if not employee:
                    employee = self.env['hr.employee'].search([
                        ('user_id', '=', current_user.id)
                    ], limit=1)
                
                # If still no employee, try by email match
                if not employee and current_user.email:
                    employee = self.env['hr.employee'].search([
                        ('work_email', '=', current_user.email),
                        ('active', '=', True)
                    ], limit=1)
                
                if employee and employee.exists():
                    # Test access to employee record
                    employee.read(['name'])
                    return employee.id
                    
            except Exception as e:
                import logging
                _logger = logging.getLogger(__name__)
                _logger.warning(f"Could not find employee for user {current_user.id}: {e}")
                
        return False

    @api.depends('date_from', 'date_to')
    def _compute_days(self):
        """Calculate number of days automatically"""
        for rec in self:
            if rec.date_from and rec.date_to:
                rec.days = (rec.date_to - rec.date_from).days + 1
            else:
                rec.days = 0

    @api.depends('days', 'destination_country_id', 'employee_id')
    def _compute_amount(self):
        """Calculate amount automatically based on days and destination"""
        for rec in self:
            if not rec.days or rec.days <= 0:
                rec.amount = 0.0
                continue
                
            # Determine national vs international based on company country
            try:
                company_country = None
                if rec.employee_id and rec.employee_id.exists():
                    if rec.employee_id.company_id and rec.employee_id.company_id.partner_id:
                        company_country = rec.employee_id.company_id.partner_id.country_id
                
                # Fallback to current company if employee company not found
                if not company_country:
                    company_country = self.env.company.partner_id.country_id
                
                # Determine if national or international
                is_national = False
                if rec.destination_country_id and company_country:
                    is_national = (rec.destination_country_id.id == company_country.id)
                
                # Apply rates per requirements: 700 DH/jour national, 1500 DH/jour international
                if is_national:
                    rate = 700.0
                else:
                    rate = 1500.0
                    
                rec.amount = rec.days * rate
                
            except Exception:
                # If error determining country, default to international rate
                rec.amount = rec.days * 1500.0

    @api.model
    def create(self, vals):
        """Override create to handle employee validation and sequence generation"""
        # Generate sequence if needed
        if vals.get('name', 'New') == 'New':
            seq = self.env['ir.sequence'].sudo().next_by_code('employee.travel') or 'TR-NEW'
            vals['name'] = seq
        
        # Force employee to current user's employee if not set or different
        current_employee = self._get_current_employee()
        if current_employee:
            vals['employee_id'] = current_employee
        elif vals.get('employee_id'):
            # If no employee found for current user but employee_id provided, validate it
            try:
                employee = self.env['hr.employee'].browse(vals['employee_id'])
                if not employee.exists():
                    raise ValidationError(_('L\'employé sélectionné n\'existe plus.'))
                # Verify this employee belongs to current user
                if employee.user_id != self.env.user:
                    raise ValidationError(_('Vous ne pouvez créer des demandes que pour votre propre compte employé.'))
            except Exception as e:
                if 'does not exist' in str(e) or 'has been deleted' in str(e):
                    raise ValidationError(_('L\'employé sélectionné n\'est plus accessible.'))
                raise
        else:
            raise ValidationError(_('Impossible de déterminer votre fiche employé. Contactez l\'administrateur.'))
        
        return super().create(vals)

    @api.depends()
    def _compute_user_rights(self):
        """Compute user rights for workflow buttons"""
        for rec in self:
            current_user = self.env.user
            
            # Employee can submit if it's their own request or they created it
            try:
                employee_user = rec.employee_id.user_id if rec.employee_id and rec.employee_id.exists() else False
                rec.can_submit = ((employee_user == current_user or 
                                 rec.create_uid == current_user) and rec.state == 'draft')
                
                # Manager can approve if they are the employee's manager or in Travel Manager group
                is_manager = False
                if rec.employee_id and rec.employee_id.exists():
                    parent_user = rec.employee_id.parent_id.user_id if rec.employee_id.parent_id else False
                    is_manager = (parent_user == current_user or 
                                 current_user.has_group('employee_travel.group_travel_manager'))
                else:
                    is_manager = current_user.has_group('employee_travel.group_travel_manager')
                    
                rec.can_approve = is_manager and rec.state in ('submitted', 'in_progress')
                
                # DAF can validate if in DAF group
                rec.can_daf_validate = (current_user.has_group('employee_travel.group_travel_daf') and 
                                       rec.state in ('approved', 'daf_review'))
                
                # Employee or manager can cancel (but not if already processed by DAF)
                rec.can_cancel = ((employee_user == current_user or is_manager) and 
                                 rec.state not in ('done', 'cancelled', 'daf_approved'))
            except Exception:
                # If there's an error accessing employee data, set conservative permissions
                rec.can_submit = rec.state == 'draft' and rec.create_uid == current_user
                rec.can_approve = (current_user.has_group('employee_travel.group_travel_manager') and 
                                  rec.state in ('submitted', 'in_progress'))
                rec.can_daf_validate = (current_user.has_group('employee_travel.group_travel_daf') and 
                                       rec.state in ('approved', 'daf_review'))
                rec.can_cancel = rec.create_uid == current_user and rec.state not in ('done', 'cancelled', 'daf_approved')

    @api.constrains('transport_mode', 'distance_km')
    def _check_plane_distance(self):
        """Enforce business rules for plane transport"""
        for rec in self:
            if rec.transport_mode == 'plane':
                if rec.distance_km < 500:
                    raise ValidationError(_('Les avions ne sont autorisés que pour des distances supérieures ou égales à 500 km. Veuillez choisir train, autocar ou véhicule de service.'))
                # Auto-set plane class based on distance
                if rec.distance_km >= 6000:
                    rec.plane_class = 'business'
                elif rec.distance_km >= 500:
                    if not rec.plane_class:  # Only set if not already set
                        rec.plane_class = 'economy'

    @api.constrains('subject')
    def _check_subject_required(self):
        """Ensure mission subject is properly filled"""
        for rec in self:
            if not rec.subject or len(rec.subject.strip()) < 5:
                raise ValidationError(_('L\'objet de la mission doit être rempli avec au moins 5 caractères (ex: Formation technique, Réunion client, Mission d\'audit).'))

    @api.constrains('date_from', 'date_to')
    def _check_dates(self):
        """Validate travel dates"""
        for rec in self:
            if rec.date_from and rec.date_to and rec.date_from > rec.date_to:
                raise ValidationError(_('La date de début doit être antérieure ou égale à la date de fin.'))
            if rec.date_from and rec.date_from < fields.Date.today():
                raise ValidationError(_('La date de début ne peut pas être dans le passé.'))

    @api.constrains('distance_km')
    def _check_distance(self):
        """Validate distance is positive"""
        for rec in self:
            if rec.distance_km and rec.distance_km <= 0:
                raise ValidationError(_('La distance doit être supérieure à 0 km.'))

    @api.constrains('order_document')
    def _check_order_document(self):
        """Validate that order document is uploaded for certain cases"""
        for rec in self:
            # Require order document for international travel or long distances
            if rec.state not in ('draft', 'cancelled') and not rec.order_document:
                is_international = (rec.destination_country_id and 
                                  rec.employee_id and rec.employee_id.company_id and
                                  rec.destination_country_id != rec.employee_id.company_id.partner_id.country_id)
                is_long_distance = rec.distance_km and rec.distance_km > 1000
                
                if is_international or is_long_distance:
                    raise ValidationError(_('L\'ordre de mission est obligatoire pour les déplacements internationaux ou les distances supérieures à 1000 km.'))

    @api.onchange('destination_country_id')
    def _onchange_destination_country(self):
        """Clear city when country changes"""
        if self.destination_country_id:
            self.destination_city_id = False
            self.destination_city = False
        return {'domain': {'destination_city_id': [('country_id', '=', self.destination_country_id.id)]}}

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        """Update fields when employee changes - but employee should be readonly"""
        if self.employee_id and self.employee_id.exists():
            try:
                # Set default destination country to company country (for national travel)
                if (self.employee_id.company_id and 
                    self.employee_id.company_id.partner_id and 
                    self.employee_id.company_id.partner_id.country_id):
                    self.destination_country_id = self.employee_id.company_id.partner_id.country_id.id
            except Exception:
                pass

    @api.onchange('distance_km', 'transport_mode')
    def _onchange_distance_transport(self):
        """Auto-update plane class and validate distance rules"""
        if self.transport_mode == 'plane' and self.distance_km:
            if self.distance_km < 500:
                return {
                    'warning': {
                        'title': 'Transport non autorisé',
                        'message': 'Les avions ne sont autorisés que pour des distances supérieures ou égales à 500 km. Veuillez choisir un autre mode de transport (train, autocar, véhicule de service).'
                    },
                    'value': {'transport_mode': False}
                }
            elif self.distance_km >= 6000:
                self.plane_class = 'business'
                return {
                    'warning': {
                        'title': 'Classe Business automatique',
                        'message': 'Pour les distances supérieures à 6000 km, les voyages se font automatiquement en classe business.'
                    }
                }
            else:
                # Distance entre 500 et 6000 km = classe économique
                self.plane_class = 'economy'
        
        # Clear vehicle if not vehicle transport
        if self.transport_mode != 'vehicle':
            self.vehicle_id = False
        
        # Clear plane class if not plane transport
        if self.transport_mode != 'plane':
            self.plane_class = False

    @api.onchange('date_from', 'date_to')
    def _onchange_dates(self):
        """Validate dates and show warning if weekend or holidays"""
        if self.date_from and self.date_to:
            if self.date_from > self.date_to:
                return {
                    'warning': {
                        'title': 'Dates invalides',
                        'message': 'La date de début doit être antérieure à la date de fin.'
                    }
                }
            
            # Calculate automatic days
            days = (self.date_to - self.date_from).days + 1
            if days > 30:
                return {
                    'warning': {
                        'title': 'Durée importante',
                        'message': f'Cette mission dure {days} jours. Veuillez vérifier que c\'est correct.'
                    }
                }

    def action_submit(self):
        """Soumettre la demande pour validation"""
        if self.state != 'draft':
            raise UserError("Seules les demandes en brouillon peuvent être soumises.")
        
        self.state = 'submitted'
        self.submitted_by = self.env.user.id
        self.submitted_date = fields.Datetime.now()
        
        # Notification automatique
        self.message_post(
            body=f"Demande de déplacement soumise par {self.employee_id.name}",
            subject="Nouvelle demande de déplacement"
        )
    
    def action_draft(self):
        """Remettre en brouillon (pour les managers)"""
        if self.state not in ('submitted', 'refused'):
            raise UserError("Cette action n'est possible que pour les demandes soumises ou refusées.")
        
        self.state = 'draft'
        self.submitted_by = False
        self.submitted_date = False
        self.refusal_reason = False
        
        self.message_post(
            body=f"Demande remise en brouillon par {self.env.user.name}",
            subject="Demande remise en brouillon"
        )

    def action_start_review(self):
        """Manager starts reviewing the request"""
        for rec in self:
            if rec.state != 'submitted':
                raise ValidationError(_('Seules les demandes soumises peuvent être mises en cours de validation.'))
            rec.state = 'in_progress'

    def action_approve_by_manager(self):
        """Manager approves the request"""
        for rec in self:
            if rec.state not in ('submitted', 'in_progress'):
                raise ValidationError(_('Cette demande ne peut pas être approuvée.'))
            rec.write({
                'state': 'approved',
                'approved_by': self.env.user.id,
                'approved_date': fields.Datetime.now(),
            })
            rec._send_notification_to_daf()

    def action_send_to_daf(self):
        """Send approved request to DAF for processing"""
        for rec in self:
            if rec.state != 'approved':
                raise ValidationError(_('Seules les demandes approuvées peuvent être envoyées à la DAF.'))
            rec.state = 'daf_review'

    def action_daf_approve(self):
        """DAF validates and processes the request"""
        for rec in self:
            if rec.state != 'daf_review':
                raise ValidationError(_('Cette demande ne peut pas être traitée par la DAF.'))
            rec.write({
                'state': 'daf_approved',
                'daf_user_id': self.env.user.id,
                'daf_date': fields.Datetime.now(),
            })

    def action_mark_done(self):
        """Mark travel as completed"""
        for rec in self:
            if rec.state != 'daf_approved':
                raise ValidationError(_('Seules les demandes validées DAF peuvent être marquées terminées.'))
            rec.state = 'done'

    def action_refuse(self):
        """Refuse the request (Manager or DAF)"""
        for rec in self:
            if rec.state in ('done', 'cancelled', 'refused'):
                raise ValidationError(_('Cette demande ne peut plus être refusée.'))
            rec.state = 'refused'

    def action_cancel(self):
        """Cancel the request (Employee or Manager)"""
        for rec in self:
            if rec.state in ('done', 'daf_approved'):
                raise ValidationError(_('Cette demande ne peut plus être annulée.'))
            rec.state = 'cancelled'

    def _send_notification_to_manager(self):
        """Send notification to manager when request is submitted"""
        for rec in self:
            try:
                if (rec.employee_id and rec.employee_id.exists() and 
                    rec.employee_id.parent_id and rec.employee_id.parent_id.user_id):
                    rec.message_post(
                        body=f"Nouvelle demande de déplacement soumise par {rec.employee_id.name}: {rec.subject}",
                        partner_ids=[rec.employee_id.parent_id.user_id.partner_id.id],
                        subtype_xmlid='mail.mt_note'
                    )
            except Exception:
                # If notification fails, log but don't block the workflow
                pass

    def _send_notification_to_daf(self):
        """Send notification to DAF group when request is approved"""
        for rec in self:
            try:
                daf_users = self.env.ref('employee_travel.group_travel_daf').users
                if daf_users:
                    partner_ids = daf_users.mapped('partner_id.id')
                    rec.message_post(
                        body=f"Demande de déplacement approuvée - À traiter: {rec.name} - {rec.subject}",
                        partner_ids=partner_ids,
                        subtype_xmlid='mail.mt_note'
                    )
            except Exception:
                # If notification fails, log but don't block the workflow
                pass
