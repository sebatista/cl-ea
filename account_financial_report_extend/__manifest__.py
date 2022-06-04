# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account Financial Report Extend",
    "summary": "Agregado de filtros por diarios",
    "version": "11.0.1.0.0",
    "development_status": "Production/Stable",
    "category": "Accounting",
    "website": "https://github.com/sebatista/EA_Jobiols",
    "author": "jeo Software",
    "maintainers": ["jobiols"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["account_financial_report"],
    "data": [
        "wizard/general_ledger_wizard_view.xml",
        "views/account_journal_views.xml",
    ],
}
