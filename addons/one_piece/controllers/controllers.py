# -*- coding: utf-8 -*-
<<<<<<< Updated upstream
from odoo import http
from odoo.http import request


class OnePiece(http.Controller):
    @http.route('/one_piece', auth='public', website = True)
    def cartas_list(self,**kwargs):
        cartas = request.env['carta.carta'].sudo().search([])
        return request.render('one_piece.web_one_piece_list',{
            'cartas':cartas
        })


    @http.route('/one_piece/<model("one.piece"):carta>', auth='public', website = True)
    def cartas_detail(self, carta,**kw):
        return http.request.render('one_piece.web_carta_detail', {
            'carta': carta
        })
=======
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class OnePieceWebsite(http.Controller):

    @http.route(['/onepiece'], type='http', auth='public', website=True)
    def index(self, **kw):
        nakamas = request.env['onepiece.card'].sudo().search([])
        return request.render("one_piece.website_list", {'nakamas': nakamas})

    @http.route(['/onepiece/<int:card_id>'], type='http', auth='public', website=True)
    def detail(self, card_id, **kw):
        card = request.env['onepiece.card'].sudo().browse(card_id)
        return request.render("one_piece.website_detail", {'card': card})
>>>>>>> Stashed changes


