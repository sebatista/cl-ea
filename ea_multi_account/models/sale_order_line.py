from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"


    @api.multi
    def _prepare_invoice_line(self, qty):
        """
        Prepare the dict of values to create the new invoice line for a sales order line.
        :param qty: float quantity to invoice

        Sobreescribimoos este metodo para seleccionar las cuentas de income de acuerdo
        al pedido de venta.
        """
        self.ensure_one()
        res = {}
        product = self.product_id.with_context(force_company=self.company_id.id)
        xxx = self.order_id.type_id.account_x
        accounts = product.product_tmpl_id._get_product_accounts()
        if xxx:
            account = accounts['income_x']
        else:
            account = accounts['income']

        if not account:
            raise UserError(_('Please define income account for this product: "%s" (id:%d) - or for its category: "%s".') %
                (self.product_id.name, self.product_id.id, self.product_id.categ_id.name))

        fpos = self.order_id.fiscal_position_id or self.order_id.partner_id.property_account_position_id
        if fpos:
            account = fpos.map_account(account)

        res = {
            'name': self.name,
            'sequence': self.sequence,
            'origin': self.order_id.name,
            'account_id': account.id,
            'price_unit': self.price_unit,
            'quantity': qty,
            'discount': self.discount,
            'uom_id': self.product_uom.id,
            'product_id': self.product_id.id or False,
            'layout_category_id': self.layout_category_id and self.layout_category_id.id or False,
            'invoice_line_tax_ids': [(6, 0, self.tax_id.ids)],
            'account_analytic_id': self.order_id.analytic_account_id.id,
            'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
        }
        return res
