##############################################################################
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
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
    "name": "multi account",
    "version": "11.0.2.0.0",
    "category": "Accounting",
    "summary": "Maneja contabilidad múltiple",
    "author": "jeo Software",
    "website": "http://github.com/jobiols/cl-ea",
    "license": "AGPL-3",
    "depends": [
        "sale_order_type",
        "product",
        "account_operating_unit",
    ],
    "data": [
        "views/sale_order_type_view.xml",
        "views/res_partner_view.xml",
        "views/product_template_view.xml",
        "views/product_category_view.xml",
        "views/account_journal.xml",
    ],
    "installable": True,
    "application": False,
}
