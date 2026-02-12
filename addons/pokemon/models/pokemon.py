# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pokemon(models.Model):
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
    image = fields.Binary()