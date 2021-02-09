from odoo import models, fields, api

class GeneralLedgerReportWizard(models.TransientModel):
    """General ledger report wizard."""

    _inherit = "general.ledger.report.wizard"

    account_journal_ids = fields.Many2many(
        'account.journal',
        string='Journals',
        required=True,
        default=lambda self: self.env['account.journal'].search([])
    )
