from odoo import models, fields


class TravelVehicle(models.Model):
    _name = 'employee.travel.vehicle'
    _description = 'Véhicule de service'

    name = fields.Char(string='Name', required=True)
    license_plate = fields.Char(string='Immatriculation')
    driver = fields.Many2one('hr.employee', string='Conducteur')
    active = fields.Boolean(default=True)
