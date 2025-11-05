from odoo import models, fields, api


class City(models.Model):
    _name = 'travel.city'
    _description = 'Ville de destination'
    _order = 'country_id, name'

    name = fields.Char(string='Nom de la ville', required=True)
    postal_code = fields.Char(string='Code postal')
    country_id = fields.Many2one('res.country', string='Pays', required=True)
    active = fields.Boolean(string='Actif', default=True)

    _sql_constraints = [
        ('name_country_unique', 'UNIQUE(name, country_id)', 
         'Une ville avec ce nom existe déjà dans ce pays!')
    ]

    def name_get(self):
        """Affichage personnalisé: Ville, Pays (Code postal)"""
        result = []
        for record in self:
            name = f"{record.name}, {record.country_id.name}"
            if record.postal_code:
                name += f" ({record.postal_code})"
            result.append((record.id, name))
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """Recherche par nom de ville, pays ou code postal"""
        if not args:
            args = []
        
        if name:
            domain = ['|', '|', 
                      ('name', operator, name),
                      ('country_id.name', operator, name),
                      ('postal_code', operator, name)]
            domain += args
            records = self.search(domain, limit=limit)
            return records.name_get()
        
        return super().name_search(name, args, operator, limit)