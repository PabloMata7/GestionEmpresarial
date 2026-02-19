# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class LorcanaWebsite(http.Controller):

<<<<<<< Updated upstream
    @http.route(['/cartas'], type='http', auth='public', website=True)
    def listar_cartas(self, **kw):
        cartas = request.env['carta'].sudo().search([])
        return request.render("lorcana.web_cartas_list", {'cartas': cartas})

    @http.route(['/cartas/<int:carta_id>'], type='http', auth='public', website=True)
=======
    @http.route(['/carta'], type='http', auth='public', website=True)
    def listar_cartas(self, **kw):
        cartas = request.env['carta'].sudo().search([])
        return request.render("lorcana.lorcana_website_list", {'cartas': cartas})

    @http.route(['/carta/<int:carta_id>'], type='http', auth='public', website=True)
>>>>>>> Stashed changes
    def detalle_carta(self, carta_id, **kw):
        carta = request.env['carta'].sudo().browse(carta_id)
        return request.render("lorcana.web_carta_detail", {'carta': carta})
