# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lorcana(models.Model):
    _name = 'lorcana.lorcana'
    _description = 'lorcana.lorcana'    

    name=fields.Char(string="Nombre", required=True)
    id=fields.Integer(string="id", required=True)
    description=fields.Char(string="Descripcion")
    franchise=fields.Char(string="Franquicia")
    colection=fields.Char(string="Coleccion")
    rarity=fields.Char(string="rareza")
    grade=fields.Char(string="Grado")
    marketValue=fields.Integer(string="PrecioMarket")
    sellValue=fields.Char(string="PrecioVenta", required=True)
    # image=fields.Binary(string="Nombre")
    
