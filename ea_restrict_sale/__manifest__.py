# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "EA Restrict Sale",
    "summary": "No permitir la modificación de Precio ni Descripcion en SO ni en Factura",
    "version": "11.0.0.0.0",
    "development_status": "Production/Stable",
    "category": "Accounting",
    "website": "https://github.com/sebatista/EA_Jobiols",
    "author": "jeo Software",
    "maintainers": ["jobiols"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'sale',
    ],
    "data": [
        'security/price_security_security.xml',
        'views/sale_order_view.xml',
    ],
    'sequence': 2
}
