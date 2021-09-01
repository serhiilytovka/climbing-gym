from odoo import models, fields


class Visits(models.Model):
    _name = "visits"

    date = fields.Datetime(string="Date of visit")
    user_id = fields.Many2one('client', string="Client ID")
