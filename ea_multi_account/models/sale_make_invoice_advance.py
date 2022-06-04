# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _
from odoo.exceptions import UserError


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        """ sobreescribimos este metodo para pasarle a la factura el tipo de venta
            Aca entra solo cuando hacen un down payment
        """
        ret = super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        ret.sale_type_id = order.type_id

        product = self.product_id
        xxx = order.type_id.account_x
        accounts = product.product_tmpl_id._get_product_accounts()
        if xxx:
            account = accounts["income_x"]
        else:
            account = accounts["income"]

        if not account:
            raise UserError(
                _(
                    'Please define income account for this product: '
                    '"%s" (id:%d) - or for its category: "%s".'
                )
                % (
                    self.product_id.name,
                    self.product_id.id,
                    self.product_id.categ_id.name,
                )
            )

        fpos = (
            order.fiscal_position_id
            or order.partner_id.property_account_position_id
        )
        if fpos:
            account = fpos.map_account(account)

        ret.invoice_line_ids.account_id = account.id

        return ret
