from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).

        Sobreescribimos este metodo para pasarle la cuenta relacionada con el tipo de venta
        """

        self.ensure_one()
        company_id = self.company_id.id
        journal_id = (self.env['account.invoice'].with_context(company_id=company_id or self.env.user.company_id.id)
            .default_get(['journal_id'])['journal_id'])
        if not journal_id:
            raise UserError(_('Please define an accounting sales journal for this company.'))

        xxx = self.type_id.account_x
        if xxx:
            account_id = self.partner_invoice_id.property_account_receivable_x_id.id
        else:
            account_id = self.partner_invoice_id.property_account_receivable_id.id

        invoice_vals = {
            'name': self.client_order_ref or '',
            'origin': self.name,
            'type': 'out_invoice',
            'account_id': account_id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'journal_id': journal_id,
            'currency_id': self.pricelist_id.currency_id.id,
            'comment': self.note,
            'payment_term_id': self.payment_term_id.id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'company_id': company_id,
            'user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id
        }
        return invoice_vals
