from odoo import models, fields


class Equipment(models.Model):
    _name = 'equipment'

    gym_id = fields.Many2one('gym', string='Gym ID')
    name = fields.Char("Equipment name", required=True)
    max_number = fields.Integer("Maximum number of people", required=True)
    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('amateur', 'Amateur'),
        ('middle', 'Middle'),
        ('Hard', 'Hard'),
    ], default='beginner', index=True)
