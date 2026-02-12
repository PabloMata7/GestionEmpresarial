# -*- coding: utf-8 -*-

from odoo import models, fields, api


""" class pokemon(models.Model):
    _name = 'pokemon.pokemon'
    _description = 'Pokemon'

    name = fields.Char()
    id = fields.Integer()
    franchise = fields.Char()
    description = fields.Text()
    colection = fields.Char()
    edition = fields.Char()
    rarity = fields.Char()
    grade = fields.Char()
    marketValue = fields.Float()
    sellValue = fields.Float()
    image = fields.Binary() """
    
class pokemon(models.Model):
    _name = 'pokemon.pokemon'
    _description = 'pokemon.pokemon'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100