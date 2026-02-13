{
    'name': "Módulo Equipo (About Us)",
    'summary': "Gestión de los miembros del equipo del proyecto",
    'description': "Módulo para presentar al equipo de alumnos",
    'author': "Rodri y equipo",
    'category': 'Website',
    'version': '0.1',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/about_us_menu.xml',
        'views/templates.xml',
        'views/about_us_views.xml',
    ],
    'application': True,
    'installable': True,
    
}