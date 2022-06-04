from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = "product.category"

    property_account_income_categ_x_id = fields.Many2one(
        "account.account",
        domain=[("internal_type", "=", "other"), ("deprecated", "=", False)],
        string="Cuenta de ingresos X",
    )
    property_account_expense_categ_x_id = fields.Many2one(
        "account.account",
        domain=[("internal_type", "=", "other"), ("deprecated", "=", False)],
        string="Cuenta de gastos X",
    )
