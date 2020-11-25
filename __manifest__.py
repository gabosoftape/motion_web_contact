# -*- encoding: utf-8 -*-
##############################################################################
#
#    Samples module for Odoo Web Login Screen
#    Copyright (C) 2019 - XUBI.ME (http://www.xubi.me)
#    @author binhnguyenxuan (https://www.linkedin.com/in/binhnguyenxuan)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#    
#    Background Source: http://forum.xda-developers.com/showpost.php?p=37322378
#
##############################################################################
{
    'name': 'Motion Web Contact Screen',
    'summary': 'The new configurable Motion Web contact Screen',
    'version': '13.0.1.0',
    'category': 'Website',
    'summary': """
            The new configurable Odoo Web Login Screen
            """,
    'author': "Gabriel Pabon LTD",
    'website': "https://www.monitoringinnovation.com",
    'license': 'AGPL-3',
    'depends': [
    ],
    'data': [
        'security/crm_security.xml',
        'views/contact_backend.xml',
        'templates/webclient_templates.xml',
        'security/ir.model.access.csv'
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/banner.png'],
}