from odoo import models, fields, api

class ColorShade(models.Model):
    _name = "product.color.shade"
    _description = "Product Color Shade"

    name = fields.Char(string="Name")
    price = fields.Float(string="Price")