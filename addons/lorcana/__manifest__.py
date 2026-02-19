# -*- coding: utf-8 -*-
{
    'name': "Lorcana",

    'summary': "Modulo de Lorcana",

    'author': "Jorge Diaz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/lorcana_views.xml',
        'views/lorcana_menu.xml'
    ],
    
    'application': True,
    'installable': True,
}

