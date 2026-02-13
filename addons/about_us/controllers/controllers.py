# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class TeamController(http.Controller):
    
    # Ruta pública [cite: 93]
    @http.route('/equipo', auth='public', website=True)
    def list_team(self, **kw):
        # Obtener todos los registros del modelo
        members = request.env['about.us.team'].search([])
        # Renderizar la plantilla pasando los datos
        return request.render('about_us.team_template', {
            'members': members
        })