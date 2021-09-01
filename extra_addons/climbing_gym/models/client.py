from odoo import models, fields


class Client(models.Model):
    _name = "client"

    firstname = fields.Char("First name", required=True)
    middlename = fields.Char("Middle name")
    lastname = fields.Char("Last name", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ])
    phone_number = fields.Char("Phone number", required=True)
    user_image = fields.Binary("Image", help="Select image here")
    user_address = fields.Char("Address")
    birthday = fields.Date("Date of birth")
    # ticket = fields.One2many()
    visits = fields.One2many('visits', 'user_id', string="User ID")
