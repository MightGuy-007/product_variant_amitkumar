from odoo import models, fields, api


class ProductPartLines(models.Model):
    _name = "product.part.lines"
    _description = "Product Part Lines"

    product_id = fields.Many2one("product.product", string="Component Product")

    qty = fields.Float("Quantity")

    unit_cost = fields.Float(related="product_id.total_cost", store=True)

    # total_cost = fields.Float(compute="_compute_total")
    total_cost = fields.Float(string="total cost")

    # @api.depends('qty', 'unit_cost')
