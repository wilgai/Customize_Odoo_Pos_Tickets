# -*- coding: utf-8 -*-
#################################################################################
# Author      : Kanak Infosystems LLP. (<https://www.kanakinfosystems.com/>)
# Copyright(c): 2012-Present Kanak Infosystems LLP.
# All Rights Reserved.
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.kanakinfosystems.com/license>
#################################################################################
{
    'name': 'POS Custom Receipt',
    'version': '1.0',
    'category': 'Point Of Sale',
    'summary': 'Customized Receipt of Point Of Sales',
    'website': 'www.wilgaisoft.net',
    'author': 'Wilgaisoft.',
    'images': ['static/description/WilgaiSoft.png'],
    'description': "Customized our point of sale receipt",
    'depends': ['base', 'point_of_sale'],
    "data": [
        "views/assets.xml"
    ],
    'demo': [],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
}
