# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Eugenio Aguirre",
    "summary": "Customizaciones varias",
    "version": "11.0.1.0.0",
    "development_status": "Production/Stable",
    "category": "Stock",
    "website": "https://github.com/sebatista/EA_Jobiols",
    "author": "jeo Software",
    "maintainers": ["jobiols"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'sale',
        'sale_order_type'
    ],
    "data": [
        'views/sale_order_view.xml',
        'views/sale_order_type_view.xml'
    ],
    'sequence': 1
}
