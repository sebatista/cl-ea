# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        """sobreescribimos este metodo para pasarle a la factura el tipo de venta"""
        ret = super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        ret.sale_type_id = order.type_id

        return ret
