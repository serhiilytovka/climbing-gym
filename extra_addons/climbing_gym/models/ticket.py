from odoo import models, fields


class Ticket(models.Model):
    _name = "ticket"

    onetime_card = fields.Boolean(string="One time ticket")
    membership_card = fields.Boolean(string="Multiple visits")
    date_from = fields.Datetime(string="Start date")
    date_due = fields.Datetime(string="Due date")
    visit_count = fields.Integer(string="Number of available visits")
    discount = fields.Integer(string="Discount %")
    price = fields.Integer(string="Price of ticket")
    service = fields.Many2many('service', string="Service")
