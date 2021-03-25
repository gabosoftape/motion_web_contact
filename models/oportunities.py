# -*- coding: utf-8 -*- #
import time
from odoo import models, fields, api


class motionOportunities(models.Model):
    _name = 'motion.crm_motion_oportunities'
    _description = 'Mensajes de contacto'
    _rec_name = 'empresa'

    empresa = fields.Char('Nombre de empresa', required=True)
    sector = fields.Char('SECTOR')
    contacto = fields.Char('CONTACTO REF')
    categoria = fields.Many2one('motion.crm_motion_op_categ', string='Categoria', required=True)
    cargo = fields.Char('CARGO REF')
    correo = fields.Char('CORREO')
    tel1 = fields.Char('TELEFONO 1')
    tel2 = fields.Char('TELEFONO 2')
    direccion = fields.Char('DIRECCIÓN')
    comentarios = fields.Text('COMENTARIOS')
    state = fields.Char('Estado Actual')

    @api.model
    def create(self, vals):
        result = super(motionOportunities, self).create(vals)
        return result


class motionOportunities(models.Model):
    _name = 'motion.crm_motion_op_categ'
    _description = 'Categoria Oportunidad'
    _rec_name = 'categoria'

    categoria = fields.Char('Nombre de Categoria', required=True)
    descripcion = fields.Text('Descripcion')
