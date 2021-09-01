from odoo import models, fields


class Gym(models.Model):
    _name = "gym"

    name = fields.Char("Gym name", required=True)
    max_number = fields.Integer("Maximum number of people", required=True)
    equipment = fields.One2many('equipment', 'gym_id', string='Gym ID')
