from odoo import models, fields, api

class UVPrinting(models.Model):
    _name = "product.uv.printing"
    _description = "Product UV Printing"

    name = fields.Char(string="Name")
    price = fields.Float(string="Price")