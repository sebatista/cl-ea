from odoo import models, fields, api, _


class AccountPaymentGroup(models.Model):
    _inherit = "account.payment.group"
    _description = "Domain en el talonario"

    operating_unit_ids = fields.Many2many(
        "operating.unit",
        "operating_unit_users_rel",
        "user_id",
        "poid",
        "Operating Units",
        default=lambda self: self.env.user.operating_unit_ids.ids,
    )
