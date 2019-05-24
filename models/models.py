# -*- coding: utf-8 -*-

from odoo import models, fields, api

class addcampus(models.Model):
    _inherit = ["res.partner"]

    contract = fields.Boolean(string='Contrato', track_visibility='onchange')
    identity = fields.Boolean(string='Copia Cedula', track_visibility='onchange')
    reception = fields.Date(string='Fecha de Recepcion', track_visibility='onchange')
    observation = fields.Text(string='Observacion')
    name = fields.Char(track_visibility='onchange')
    vat = fields.Char(track_visibility='onchange')
    mobile = fields.Char(track_visibility='onchange')
    email = fields.Char(track_visibility='onchange')
    phone = fields.Char(track_visibility='onchange')


