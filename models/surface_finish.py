from odoo import models, fields, api

class SurfaceFinish(models.Model):
    _name = 'product.surface.finish'
    _description = 'Product Surface Finish'

    name = fields.Char(string="Name")
    amount = fields.Float(string="Amount")


    