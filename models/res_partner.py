from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_name = fields.Char(string="Nombre Empresa")
    sector = fields.Char(string="Sector Empresa")
    observaciones = fields.Text(string="Observaciones")
    status_now = fields.Text(string="Estado actual")
