# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class TeamController(http.Controller):

    @http.route('/equipo', auth='public', website=True)
    def list_team(self, **kw):
        members = request.env['about.us'].search([])
        return request.render('about_us.view_equipo_final', {
            'members': members
        })