from odoo import models, fields, api


class ProductPartLines(models.Model):
    _name = "product.part.lines"
    _description = "Product Part Lines"

    parent_product_id = fields.Many2one("product.product", string="Parent Product", ondelete="cascade")

    is_multi_parts = fields.Boolean(related="parent_product_id.is_multi_parts", store=False, string="Is Multi Parts")

    product_id = fields.Many2one("product.product",string="Component Product",
        domain="[('type', 'in', ['accessories', 'product', 'subproduct'])]",
    )

    line_type = fields.Selection(related="product_id.type", string="Component Type", store=True, readonly=True)

    qty = fields.Float("Quantity", default=1.0)

    unit_cost = fields.Float(related="product_id.total_cost", store=True, string="Unit Cost", readonly=True)

    component_cost = fields.Float(compute="_compute_component_cost", store=True, string="Component Cost")


    accessories = fields.Float("Accessories", store=True, readonly=True, compute="_compute_component_cost")
    sub_products = fields.Float("Sub Products", store=True, readonly=True, compute="_compute_component_cost")

    # ──────────────────────────────────────────────────────────
    @api.depends("qty", "unit_cost")
    def _compute_component_cost(self):
        for rec in self:
            if rec.line_type == "accessories":
                rec.component_cost = rec.qty * rec.unit_cost
                rec.accessories = rec.component_cost

            elif rec.line_type == "product" or rec.line_type == "subproduct":
                rec.component_cost = rec.qty * rec.unit_cost
                rec.sub_products = rec.component_cost