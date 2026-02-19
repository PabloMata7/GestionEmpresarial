# -*- coding: utf-8 -*-

from odoo import models, fields, api


class carta(models.Model):
    _name = 'onepiece.card'  # <--- NOMBRE ÚNICO (Namespace)
    _description = 'Carta de One Piece'

    name = fields.Char(string="Nombre", required=True)
    card_id = fields.Char(string="Código Carta", required=True) # Ej: OP01-001
    
    # Datos específicos de One Piece
    type_card = fields.Selection([
        ('leader', 'Líder'),
        ('character', 'Personaje'),
        ('event', 'Evento'),
        ('stage', 'Escenario')
    ], string="Tipo")
    
    color = fields.Selection([
        ('red', 'Rojo'),
        ('green', 'Verde'),
        ('blue', 'Azul'),
        ('purple', 'Morado'),
        ('black', 'Negro'),
        ('yellow', 'Amarillo')
    ], string="Color")

    power = fields.Integer(string="Poder (Power)")
    rarity = fields.Char(string="Rareza") # Ej: SR, L, R
    
    # Precios (Float para evitar errores de cálculo)
    marketValue = fields.Float(string="Precio Mercado", digits=(10, 2))
    sellValue = fields.Float(string="Precio Venta", required=True, digits=(10, 2))
    
    description = fields.Text(string="Efecto / Descripción")
    image = fields.Binary(string="Imagen")

