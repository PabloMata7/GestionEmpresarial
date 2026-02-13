# -*- coding: utf-8 -*-
from odoo import models, fields

class AboutUs(models.Model):
    _name = 'about.us'
    _description = 'Miembros del Equipo del Proyecto'
    name = fields.Char(string="Nombre del Alumno", required=True)
    role = fields.Char(string="Rol / Módulo Desarrollado", required=True)
    description = fields.Text(string="Descripción")
    image = fields.Binary(string="Fotografía", attachment=True)

    rarity = fields.Char(string="Nivel de Rareza", help="Ej: Legendario, Épico")
    grade = fields.Char(string="Nota Esperada", help="Ej: 10/10")