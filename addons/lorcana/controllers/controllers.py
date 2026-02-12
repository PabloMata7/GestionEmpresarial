# -*- coding: utf-8 -*-
# from odoo import http


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

