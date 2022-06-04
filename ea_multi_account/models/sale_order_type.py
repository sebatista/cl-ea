from odoo import models, fields, api


class SaleOrderType(models.Model):
    _inherit = "sale.order.type"

    account_x = fields.Boolean(string="XXX")
