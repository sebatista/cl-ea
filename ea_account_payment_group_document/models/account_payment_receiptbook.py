from odoo import models, fields


class AccountPaymentReceiptbook(models.Model):

    _inherit = "account.payment.receiptbook"
    _description = "campo unidad de opración"

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Operating Unit",
    )
