from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    property_account_receivable_x_id = fields.Many2one(
        'account.account',
        domain="[('internal_type', '=', 'receivable'),('deprecated', '=', False)]",
        required=True,
        string="Cuenta a cobrar X",
        default=lambda self: self.default_receivable_x()
    )
    property_account_payable_x_id = fields.Many2one(
        'account.account',
        domain="[('internal_type', '=', 'payable'),('deprecated', '=', False)]",
        required=True,
        string="Cuenta a pagar X",
        default=lambda self: self.default_payable_x()
    )

    def default_receivable_x(self):
        config = self.env["ir.config_parameter"].sudo()
        code = config.get_param('receivable_account_x')
        return self.env['account.account'].search([('code', '=', code)])

    def default_payable_x(self):
        config = self.env["ir.config_parameter"].sudo()
        code = config.get_param('payable_account_x')
        return self.env['account.account'].search([('code', '=', code)])
