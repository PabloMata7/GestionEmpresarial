# -*- coding: utf-8 -*-

from odoo import models, fields, api


class carta(models.Model):
<<<<<<< Updated upstream
    _name = 'carta.carta'
    _description = 'carta.carta'

    name = fields.Char(string = "Nombre", required = True)
    card_id = fields.Integer(string = "Card ID", required = True)
    franchise = fields.Char(string = "Franquicia")
    description = fields.Text(string = "Descripción")
    colection = fields.Char(string = "Colección")
    edition = fields.Char(string = "Edición")
    rarity = fields.Char(string = "Rareza")
    grade = fields.Char(string = "Valoración")
    marketValue = fields.Float(string = "Precio de mercado")
    sellValue = fields.Float(string = "Precio de venta",required = True)
    image = fields.Binary(string = "Imagen")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
=======
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
>>>>>>> Stashed changes

