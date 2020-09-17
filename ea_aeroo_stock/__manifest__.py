# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Reporte de stock aeroo",
    "summary": "Remito Modificado para Eugenio Aguirre",
    "version": "11.0.0.0.0",
    "development_status": "Alpha",  # "Alpha|Beta|Production/Stable|Mature"
    "category": "Stock",
    "website": "https://github.com/sebatista/ea_jobiols",
    "author": "jeo Software",
    "maintainers": ["jobiols"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'l10n_ar_aeroo_stock',
        'base',
    ],
    "data": [
        'report/invoice_report.xml',
    ],
    'sequence': 1
}
