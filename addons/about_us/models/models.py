# -*- coding: utf-8 -*-

from odoo import models, fields

class AboutUsTeam(models.Model):
    _name = 'about.us.team'
    _description = 'Miembros del Equipo del Proyecto'

    # 1. Nombre del miembro (Obligatorio según el PDF)
    name = fields.Char(
        string='Nombre del Alumno', 
        required=True,
        help="Nombre completo del integrante del grupo"
    )

    # 2. Rol dentro del proyecto / Módulo desarrollado (Obligatorio)
    role = fields.Char(
        string='Rol / Módulo Desarrollado', 
        required=True,
        help="Ej: Desarrollador del módulo de Inventario"
    )

    # 3. Descripción breve (Obligatorio)
    description = fields.Text(
        string='Descripción',
        help="Breve descripción sobre el estudiante o sus tareas"
    )

    # 4. Fotografía (Obligatorio: campo imagen)
    image = fields.Binary(
        string='Fotografía',
        attachment=True,
        help="Foto del miembro del equipo"
    )