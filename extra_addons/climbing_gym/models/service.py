from odoo import models, fields


class Service(models.Model):
    _name = "service"

    name = fields.Char("Name of Service")
    price = fields.Char("Price of service")
