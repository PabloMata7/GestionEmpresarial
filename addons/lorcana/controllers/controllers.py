# -*- coding: utf-8 -*-

# class Lorcana(http.Controller):
#     @http.route('/lorcana/lorcana', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lorcana/lorcana/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lorcana.listing', {
#             'root': '/lorcana/lorcana',
#             'objects': http.request.env['lorcana.lorcana'].search([]),
#         })

#     @http.route('/lorcana/lorcana/objects/<model("lorcana.lorcana"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lorcana.object', {
#             'object': obj
#         })

from odoo import http
from odoo.http import request

@http.route(['/carta'], type='http', auth='public', website=True)
def listar_cartas(self, **kw):
    cartas = request.env['carta'].sudo().search([])
    return request.render("lorcana.lorcana_website_list", {'cartas': cartas})

@http.route(['/carta/<int:carta_id>'], type='http', auth='public', website=True)
def detalle_carta(self, carta_id, **kw):
    carta = request.env['carta'].sudo().browse(carta_id)
    return request.render("lorcana.web_carta_detail", {'carta': carta})
