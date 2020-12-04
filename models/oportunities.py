# -*- coding: utf-8 -*- #
import time
from odoo import models, fields, api


class motionOportunities(models.Model):
    _name = 'motion.crm_motion_oportunities'
    _description = 'Mensajes de contacto'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre')
    empresa = fields.Char('EMPRESA')
    categoria = fields.Char('CATEGORIA')
    contacto = fields.Char('CONTACTO REF')
    cargo = fields.Char('CARGO REF')
    correo = fields.Char('CORREO')
    tel1 = fields.Char('TELEFONO 1')
    tel2 = fields.Char('TELEFONO 2')
    direccion = fields.Char('DIRECCIÓN')
    comentarios = fields.Char('COMENTARIOS')
    fecha = fields.Datetime('FECHA DE GESTIÓN INICIAL')
    state = fields.Selection(
        [('cancelado', 'Descartado'), ('nuevo', 'Prospecto'), ('sin concretar', 'Pendiente (sin concretar)'), ('concretado', 'Concretado')],
        'Estado', default='nuevo')

    @api.model
    def create(self, vals):
        result = super(motionOportunities, self).create(vals)
        return result
