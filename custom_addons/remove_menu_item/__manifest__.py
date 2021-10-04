# -*- coding: utf-8 -*-
{
    'name': "remove_menu_item",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Wilgaisoft",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
         'views/ir_module_view.xml',
    ],
  'qweb': ["static/src/xml/base.xml",
           "static/src/xml/pos_logo.xml",
           ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
