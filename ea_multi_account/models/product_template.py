from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    property_account_income_x_id = fields.Many2one(
        "account.account",
        domain=[("internal_type", "=", "other"), ("deprecated", "=", False)],
        string="Cuenta de ingresos X",
    )
    property_account_expense_x_id = fields.Many2one(
        "account.account",
        domain=[("deprecated", "=", False)],
        string="Cuenta de gastos X",
    )

    @api.multi
    def _get_product_accounts(self):
        """Sobreescribimos este metodo para devolver las nuevas cuentas"""
        return {
            "income": self.property_account_income_id
            or self.categ_id.property_account_income_categ_id,
            "expense": self.property_account_expense_id
            or self.categ_id.property_account_expense_categ_id,
            "income_x": self.property_account_income_x_id
            or self.categ_id.property_account_income_categ_x_id,
            "expense_x": self.property_account_expense_x_id
            or self.categ_id.property_account_expense_categ_x_id,
        }
