# -*- coding: utf-8 -*-
# from odoo import http


# class OnePiece(http.Controller):
#     @http.route('/one_piece/one_piece', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/one_piece/one_piece/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('one_piece.listing', {
#             'root': '/one_piece/one_piece',
#             'objects': http.request.env['one_piece.one_piece'].search([]),
#         })

#     @http.route('/one_piece/one_piece/objects/<model("one_piece.one_piece"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('one_piece.object', {
#             'object': obj
#         })

