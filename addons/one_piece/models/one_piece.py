# -*- coding: utf-8 -*-

from odoo import models, fields, api


class one_piece(models.Model):
    _name = 'one_piece.one_piece'
    _description = 'one_piece.one_piece'

    name = fields.Char(string = "nombre", required = True)
    id = fields.Integer(string = "ID", required = True)
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

