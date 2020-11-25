# -*- coding: utf-8 -*- #
import time
from odoo import models, fields, api


class motionContact(models.Model):
    _name = 'motion.crm_contact'
    _description = 'Mensajes de contacto'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre')
    state = fields.Selection(
        [('cancelado', 'Cancelado'), ('nuevo', 'Nuevo'), ('creado', 'Completo'), ('validado', 'Validado')],
        'Estado', default='nuevo')
    telefono = fields.Char('Telefono')
    asunto = fields.Char('Asunto')
    solicitud = fields.Char('Solicitud')
    email = fields.Char('Correo Electronico')
    empresa = fields.Char('Empresa')
    medio = fields.Selection(
        [('fb', 'Facebook'), ('sw', 'Sitio Web'), ('ig', 'Instagram'), ('tg', 'Telegram')],
        'Medio', default='fb')

    @api.model
    def create(self, vals):
        result = super(motionContact, self).create(vals)
        return result
