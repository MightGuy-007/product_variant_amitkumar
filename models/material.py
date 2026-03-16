from odoo import models, fields, api

class Material(models.Model):
    _name = "product.material"
    _description = "Product Material"

    name = fields.Char(string="Name")
    price = fields.Float(string="Price")