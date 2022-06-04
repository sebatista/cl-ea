from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "account.invoice"

    @api.onchange("sale_type_id")
    def _compute_domain(self):
        """Genera el dominio para filtrar los tipos de pedido de ventas en funcion
        de las operating units del usuario.
        """
        # ou del usuario
        ou_ids = self.env.user.operating_unit_ids

        # las type que tienen la ou del usuario
        domain = [("operating_unit_id.id", "in", ou_ids.ids)]
        type_ids = self.env["sale.order.type"].search(domain)

        # las type que no tienen ou
        domain = [("operating_unit_id", "=", False)]
        type_ids |= self.env["sale.order.type"].search(domain)

        domain = {"sale_type_id": [("id", "in", type_ids.ids)]}
        return {"domain": domain}
