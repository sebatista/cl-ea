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
        'https://github.com/sebatista/EA_Jobiols.git',

        'https://github.com/jobiols/odoo-addons.git',
        'https://github.com/oca/server-brand',
        'https://github.com/ingadhoc/account-invoicing',




        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/account-payment.git ingadhoc-account-payment',
        'https://github.com/ingadhoc/miscellaneous.git',
        'https://github.com/ingadhoc/argentina-reporting.git',
        'https://github.com/ingadhoc/reporting-engine.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/sale.git ingadhoc-sale',
        'https://github.com/ingadhoc/product.git ingadhoc-product',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/stock.git',

        'https://github.com/oca/partner-contact.git',
        'https://github.com/oca/web.git',
        'https://github.com/oca/website.git oca-website',
        'https://github.com/oca/account-financial-reporting.git',
        'https://github.com/oca/social.git',
        'https://github.com/oca/account-payment.git oca-account-payment',
        'https://github.com/oca/operating-unit.git oca-operating-unit',
        'https://github.com/oca/commission.git oca-commission',
        'https://github.com/oca/account-financial-tools.git oca-account-financial-tools',
        'https://github.com/oca/reporting-engine.git oca-reporting-engine',

        'https://github.com/oca/server-tools.git oca-server-tools',
        'https://github.com/oca/stock-logistics-workflow.git oca-stock-logistics-workflow',
        'https://github.com/oca/sale-workflow.git oca-sale-workflow',
        'https://github.com/oca/stock-logistics-warehouse.git oca-stock-logistics-warehouse',
        'https://github.com/oca/server-ux.git oca-server-ux',

        'https://github.com/itpp-labs/access-addons.git itpp-labs-access-addons',
        'https://github.com/itpp-labs/mail-addons.git itpp-mail-addons',
        'https://github.com/itpp-labs/misc-addons.git itpp-misc-addons',
        'https://github.com/itpp-labs/website-addons.git itpp-misc-addons',
        #'https://github.com/sebatista/EA_theme_laze.git seba-theme-laze -b main',
        'git@github.com:sebatista/EA_theme_laze.git tema',
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
