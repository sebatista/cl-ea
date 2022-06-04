from odoo import models, fields, api


class SaleOrderType(models.Model):
    _inherit = "sale.order.type"

    operating_unit_id = fields.Many2one("operating.unit")
