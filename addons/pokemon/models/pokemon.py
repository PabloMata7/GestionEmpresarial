# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pokemon(models.Model):
    _name = 'pokemon.pokemon'
    _description = 'Pokemon'
    
    name = fields.Char(string = "Nombre", required=True)
    id = fields.Integer(string = "ID", required=True)
    franchise = fields.Char(string = "Franquicia")
    description = fields.Text(string = "Descripcion")
    colection = fields.Char(string = "Coleccion")
    edition = fields.Char(string = "Edicion")
    rarity = fields.Char(string = "Rareza")
    grade = fields.Char(string = "Grado")
    marketValue = fields.Float(string = "Precio de Mercado")
    sellValue = fields.Float(string = "Precio de Venta", required=True)
    image = fields.Binary(string = "Imagen") 
    
""" class pokemon(models.Model):
    _name = 'pokemon.pokemon'
    _description = 'pokemon.pokemon'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100 """