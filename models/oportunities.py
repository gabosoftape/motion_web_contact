# -*- coding: utf-8 -*- #
import time
from odoo import models, fields, api


class motionOportunities(models.Model):
    _name = 'motion.crm_motion_oportunities'
    _description = 'Mensajes de contacto'
    _rec_name = 'empresa'

    empresa = fields.Char('Nombre de empresa', required=True)
    categoria = fields.Many2one('motion.crm_motion_op_categ', string='Categoria', required=True)
    contacto = fields.Char('CONTACTO REF')
    cargo = fields.Char('CARGO REF')
    correo = fields.Char('CORREO')
    tel1 = fields.Char('TELEFONO 1')
    tel2 = fields.Char('TELEFONO 2')
    direccion = fields.Char('DIRECCIÓN')
    comentarios = fields.Text('COMENTARIOS')
    fecha = fields.Datetime('FECHA DE GESTIÓN INICIAL')
    state = fields.Selection(
        [('cancelado', 'Descartado'), ('nuevo', 'Prospecto'), ('sin concretar', 'Pendiente (sin concretar)'), ('concretado', 'Concretado')],
        'Estado', default='nuevo')

    @api.model
    def create(self, vals):
        result = super(motionOportunities, self).create(vals)
        return result


class motionOportunities(models.Model):
    _name = 'motion.crm_motion_op_categ'
    _description = 'Categoria Oportunidad'
    _rec_name = 'empresa'

    categoria = fields.Char('Nombre de empresa', required=True)
    descripcion = fields.Text('Descripcion')
