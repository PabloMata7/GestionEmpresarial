# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class PokemonWebsite(http.Controller):

    # @http.route define la URL, el tipo de autenticación y si usa el framework website
    @http.route('/pokemon', auth='public', website=True)
    def index(self, **kwargs):
        # 1. Acceso a la DB (ORM)
        # request.env es tu puntero al entorno global (Registry + Cursor DB + Usuario)
        # Esto es equivalente a un "SELECT * FROM pokemon"
        pokemons = request.env['pokemon'].sudo().search([])

        # 2. Renderizado
        # Pasamos el string del ID del template y un diccionario de contexto (las variables)
        return request.render('pokemon.pokemon_website_list', {
            'pokemons': pokemons,
        })
        
    @http.route('/pokemon/<model("pokemon"):carta>', auth='public', website=True)
    def detail(self, carta, **kw):
        return http.request.render('pokemon.pokemon_website_detail', {
            'pokemon': carta, # Pasamos el objeto singular a la vista
        })

