from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class AccountInvoice(models.Model):
    _inherit = "account.invoice.line"

    @api.v8
    def get_invoice_line_account(self, type, product, fpos, company):
        """ Sobreescribimos este metodo para traer las cuentas X cuando corresponde
        """
        for rec in self:
            accounts = product.product_tmpl_id.get_product_accounts(fpos)
            account_x = rec.invoice_id.sale_type_id.account_x
            if type in ('out_invoice', 'out_refund'):
                if account_x:
                    return accounts['income_x']
                else:
                    return accounts['income']

            if account_x:
                return accounts['expense_x']
            else:
                return accounts['expense']
