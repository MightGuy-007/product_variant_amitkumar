from odoo import fields, models, api


class ProductVariant(models.Model):
    _inherit = "product.product"

    is_multi_parts = fields.Boolean(string="Multi Part")

    type = fields.Selection(
        [
            ("product", "Product"),
            ("subproduct", "Sub Product"),
            ("accessories", "Accessories"),
        ],
        default="subproduct",
        string="Product Type",
    )

    material_id = fields.Many2one("product.material", string="Material")
    surface_finish_id = fields.Many2one("product.surface.finish", string="Surface Finish")
    uv_printing_id = fields.Many2one("product.uv.printing", string="UV Printing")
    color_shade_id = fields.Many2one("product.color.shade", string="Color Shade")

    product_cost = fields.Float("Product Cost", readonly=True)
    accessories_cost = fields.Float("Accessories Cost", readonly=True)
    total_cost = fields.Float(compute="_compute_total_cost", store=True, string="Total Cost")

    parts_lines_ids = fields.One2many(
        "product.part.lines",
        "parent_product_id",
        string="Part Lines",
    )

    # ─────────────────────────────────────────────────────────────────────────
    @api.depends(
        "material_id",
        "surface_finish_id",
        "uv_printing_id",
        "color_shade_id",
        "parts_lines_ids.component_cost",
        "parts_lines_ids.line_type",
    )
    def _compute_total_cost(self):
        for rec in self:
            # if rec.material_id else 0.0
            spec_cost = (
                  rec.material_id.price
                + rec.surface_finish_id.price
                + rec.uv_printing_id.price
                + rec.color_shade_id.price
            )


            accessories = sum(rec.parts_lines_ids.mapped("accessories"))
            sub_products = sum(rec.parts_lines_ids.mapped("sub_products"))

            rec.product_cost = sub_products
            rec.accessories_cost = accessories
            rec.total_cost = spec_cost + accessories + sub_products