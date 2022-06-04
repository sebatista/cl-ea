from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    delivery_address_id = fields.Many2one(
        "res.partner", compute="_compute_delivery_address"
    )

    @api.depends("type")
    def _compute_delivery_address(self):

        for rec in self:
            delivery = rec.child_ids.filtered(lambda r: r.type == "delivery")
            rec.delivery_address_id = delivery[0] if delivery else rec
