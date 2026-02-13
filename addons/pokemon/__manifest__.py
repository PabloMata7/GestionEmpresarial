# -*- coding: utf-8 -*-
{
    'name': "pokemon",

    'summary': "Modulo de Pokemon",

    'author': "Pablo Mata",

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
        'views/pokemon_views.xml',
        'views/pokemon_menu.xml'
    ],
    
    'application': True,
    'installable': True,
}

