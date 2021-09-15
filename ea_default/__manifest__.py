##############################################################################
#
#    Copyright (C) 2020  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'EA',
    'version': '11.0.1.0.0',
    'category': 'Tools',
    'summary': "Eugenio Aguirre project module",
    'author': "jeo Software",
    'website': 'http://github.com/jobiols/cl-ea',
    'license': 'AGPL-3',
    'depends': [
        'account_financial_report_extend',
        'ea_aeroo_stock',
        'ea_custom',
        'ea_multi_account',
        'ea_restrict_sale',
        'crm_operating_unit',
        'sales_team_operating_unit',
        'account_operating_unit',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    'config': [
    ],

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/sebatista/EA_Jobiols',
		'git@github.com:sebatista/garazd_website sise-garazd_website',
        'git@github.com:sebatista/EA_theme_laze tema',
		
		'https://github.com/sebatista/jobiols-odoo-addons sise-jobiols-odoo-addons',
        'https://github.com/jobiols/odoo-addons jeo-odoo-addons',
		
		'https://github.com/regaby/odoo-addons regaby-odoo-addons',
		
		'https://github.com/akretion/odoo-usability akretion-odoo-usability',
		
        'https://github.com/ingadhoc/account-invoicing adhoc-account-invoicing',
        'https://github.com/ingadhoc/odoo-argentina.git adhoc-odoo-argentina',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/account-payment.git adhoc-account-payment',
        'https://github.com/ingadhoc/miscellaneous.git',
        'https://github.com/ingadhoc/argentina-reporting.git',
        'https://github.com/ingadhoc/reporting-engine.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/sale.git ingadhoc-sale',
        'https://github.com/ingadhoc/product.git ingadhoc-product',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/stock adhoc-stock',
		'https://github.com/ingadhoc/multi-store adhoc-multi-store',

        'https://github.com/oca/server-brand oca-server-brand',
		'https://github.com/OCA/account-analytic oca-account-analytic',
		'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting',
		'https://github.com/OCA/account-financial-tools oca-account-financial-tools',
		'https://github.com/OCA/account-invoicing oca-account-invoicing',
		'https://github.com/OCA/account-payment oca-account-payment',
		'https://github.com/OCA/commission oca-commission',
		'https://github.com/OCA/contract oca-contract',
		'https://github.com/OCA/credit-control.git oca-credit-control',
		'https://github.com/OCA/crm oca-crm',
		'https://github.com/OCA/e-commerce oca-e-commerce',
		'https://github.com/OCA/hr oca-hr',
		'https://github.com/OCA/hr-timesheet oca-hr-timesheet',
		'https://github.com/OCA/knowledge oca-knowledge',
		'https://github.com/OCA/manufacture oca-manufacture',
		'https://github.com/OCA/margin-analysis oca-margin-analysis',
		'https://github.com/OCA/operating-unit.git oca-operating-unit',
		'https://github.com/OCA/partner-contact oca-partner-contact',
		'https://github.com/OCA/product-attribute oca-product-attribute',
		'https://github.com/OCA/product-variant oca-product-variant',
		'https://github.com/OCA/purchase-workflow oca-purchase-workflow',
		'https://github.com/OCA/queue oca-queue',
		'https://github.com/OCA/reporting-engine oca-reporting-engine',
		'https://github.com/OCA/report-print-send oca-report-print-send',
		'https://github.com/OCA/sale-financial oca-sale-financial',
		'https://github.com/OCA/sale-reporting.git oca-sale-reporting',
		'https://github.com/OCA/sale-workflow oca-sale-workflow',
		'https://github.com/OCA/server-tools oca-server-tools',
		'https://github.com/OCA/server-ux oca-server-ux',
		'https://github.com/OCA/social oca-social',
		'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse',
		'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow',
		'https://github.com/OCA/web oca-web',
		'https://github.com/OCA/website oca-website',


        'https://github.com/itpp-labs/access-addons itpp-labs-access-addons',
        'https://github.com/itpp-labs/mail-addons itpp-mail-addons',
        'https://github.com/itpp-labs/misc-addons itpp-misc-addons',
        'https://github.com/itpp-labs/website-addons itpp-website-addons',
		
    ],

    # list of images to use in the form 'name image-url'
    # se usa imagen 11.1 que incluye requerimientos para website_multi_theme
    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres postgres:10.1-alpine',
        'aeroo jobiols/aeroo-docs',
        'nginx nginx'
    ]
}
