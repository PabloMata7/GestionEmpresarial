{
    'name': "Módulo Equipo (About Us)",
    'summary': "Gestión de los miembros del equipo del proyecto",
    'description': "Módulo obligatorio para presentar al equipo de alumnos",
    'author': "Rodri y equipo",
    'category': 'Website',
    'version': '0.1',
    'depends': ['base', 'website'],  # [cite: 90] Dependencia necesaria para controladores web
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/about_us_menu.xml',      #  Menús separados
        'views/templates.xml',  # [cite: 92] Plantillas QWeb
        'views/about_us_views.xml',
    ],
    'application': True,
    'installable': True,
    
}