from odoo import fields, models, api

class ProductVariant(models.Model):
    _inherit = "product.product"

    is_multi_parts = fields.Boolean(string="Multi Part")

    material_id = fields.Many2one('product.material', string="Material")
    surface_finish_id = fields.Many2one('product.surface.finish', string="Surface Finish")
    uv_printing_id = fields.Many2one('product.uv.printing', string="UV Printing")
    color_shade_id = fields.Many2one('product.color.shade', string="Color Shade")

    total_cost = fields.Float(compute="_compute_total_cost", store=True, string="Total Cost")

    parts_lines_ids = fields.One2many('product.part.lines', 'product_id', string="Part Lines")


    @api.depends('material_id','surface_finish_id','uv_printing_id','color_shade_id')
    def _compute_total_cost(self):
        for rec in self:
            rec.total_cost = (
                    rec.material_id.price +
                    rec.surface_finish_id.price +
                    rec.uv_printing_id.price +
                    rec.color_shade_id.price
            )

