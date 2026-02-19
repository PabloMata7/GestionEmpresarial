# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Lorcana(models.Model):
    _name = 'carta'
    _description = 'Carta de Lorcana'    

    name = fields.Char(string="Nombre", required=True)
    carta_id = fields.Char(string="ID Carta", required=True)
    description = fields.Text(string="Descripción")
    franchise = fields.Char(string="Franquicia")
    colection = fields.Char(string="Colección")
    rarity = fields.Char(string="Rareza")
    grade = fields.Char(string="Grado")
    marketValue = fields.Float(string="Precio Mercado", digits=(10, 2))
    sellValue = fields.Float(string="Precio Venta", required=True, digits=(10, 2))    
    image = fields.Binary(string="Imagen")
    
