from odoo import models, fields, api, _


class AccountPaymentGroup(models.Model):
    _inherit = "account.payment.group"
    _description = "Domain en el talonario"

    operating_unit_ids = fields.Many2many(
        "operating.unit",
        compute="compute_unit_ids",
        default=lambda self: self.env.user.operating_unit_ids.ids,
    )

    def compute_unit_ids(self):

        ou_ids = self.env.user.operating_unit_ids

        for record in self:
            if ou_ids:
                record.operating_unit_ids = ou_ids.ids
            else:
                record.operating_unit_ids = None

    @api.multi
    def _get_receiptbook(self):

        self.ensure_one()
        partner_type = self.partner_type or self._context.get(
            "partner_type", self._context.get("default_partner_type", False)
        )
        ou_ids = self.env.user.operating_unit_ids
        if ou_ids:
            receiptbook = self.env["account.payment.receiptbook"].search(
                [
                    ("partner_type", "=", partner_type),
                    ("company_id", "=", self.company_id.id),
                    ("operating_unit_id", "in", ou_ids.ids),
                ],
                limit=1,
            )
        else:
            receiptbook = self.env["account.payment.receiptbook"].search(
                [
                    ("partner_type", "=", partner_type),
                    ("company_id", "=", self.company_id.id),
                ],
                limit=1,
            )
        return receiptbook
