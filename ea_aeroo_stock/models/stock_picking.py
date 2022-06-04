from odoo import models, fields, api


class Picking(models.Model):
    _inherit = "stock.picking"

    picking_invoice = fields.Char(compute="_compute_picking_invoice")

    @api.depends("origin")
    def _compute_picking_invoice(self):

        so_obj = self.env["sale.order"]
        for rec in self:
            so = so_obj.search([("name", "=", rec.origin)])
            if so and so.invoice_ids:
                for invoice in so.invoice_ids:
                    rec.picking_invoice = invoice.display_name
                    break
