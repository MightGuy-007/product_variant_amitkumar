from odoo import models, fields, api


class ProductPartLines(models.Model):
    _name = "product.part.lines"

    product_id = fields.Many2one("product.product", string="Component Product")

    qty = fields.Float("Quantity")

    unit_cost = fields.Float(related="product_id.total_cost", store=True, string="Unit Cost")

    component_cost = fields.Float(compute="_compute_total")

    @api.depends('qty', 'unit_cost')
    def _compute_total(self):
        for rec in self:
            rec.component_cost = rec.qty * rec.unit_cost