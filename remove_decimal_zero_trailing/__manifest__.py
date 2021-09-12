# -*- coding: utf-8 -*-
# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

{
    'name': "Remove Decimal Zero Trailing",

    'summary': """
        This module enable you to remove decimal zero trailing in all Odoo views and reports.
        """,
    'description': """
Remove Decimal Zero Trailing
odoo Decimal Precision
Decimal Precision
Decimal Precision drop zeros
Hide Decimal Zero Trailing
    """,

    'author': 'Wilgaisoft.',
    'website': 'http://www.wilgaisoft.net.net',
    'license': 'OPL-1',
    'support': 'support@wilgaisoft.net',


    'category': 'Extra Tools',
    'version': '13.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': [ 'base'],
    # always loaded
    'data': [
        "views/templates.xml",
    ],
    'images': [],
    "installable": True
}
