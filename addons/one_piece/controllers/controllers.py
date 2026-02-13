# -*- coding: utf-8 -*-
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


