from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    property_account_receivable_x_id = fields.Many2one(
        'account.account',
        domain="[('internal_type', '=', 'receivable'),('deprecated', '=', False)]",
        required=True,
        string="Cuenta a cobrar X"
    )
    property_account_payable_x_id = fields.Many2one(
        'account.account',
        domain="[('internal_type', '=', 'payable'),('deprecated', '=', False)]",
        required=True,
        string="Cuenta a pagar X"
    )
