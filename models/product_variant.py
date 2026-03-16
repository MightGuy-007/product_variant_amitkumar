from odoo import fields, models, api

class ProductVariant(models.Model):
    _inherit = "product.product"

    is_multi_parts = fields.Boolean(string="Multi Part")

    material = fields.Char(string="Material")
    # surface_finish = fields.Many2one(string="Surface Finish")
