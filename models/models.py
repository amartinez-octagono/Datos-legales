# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.misc import format_date

class addcampus(models.Model):
    _inherit = ["res.partner"]

    contract = fields.Boolean(string='Contrato', track_visibility='onchange')
    identity = fields.Boolean(string='Copia Cedula', track_visibility='onchange')
    reception = fields.Date(string='Fecha de Recepcion', track_visibility='onchange')
    observation = fields.Text(string='Observacion')
    name = fields.Char(track_visibility='onchange', index=True)
    vat = fields.Char(track_visibility='onchange', string='TIN', help="Tax Identification Number. "
                                         "Fill it if the company is subjected to taxes. "
                                         "Used by the some of the legal statements.")
    mobile = fields.Char(track_visibility='onchange')
    email = fields.Char(track_visibility='onchange')
    phone = fields.Char(track_visibility='onchange')

class mail_contact(models.Model):
#     _inherit = ['ir.needaction_mixin']
    _inherit = 'mail.message'

    @api.model
    def _get_reply_to(self, values):
        """ Return a specific reply_to: alias of the document through
        message_get_reply_to or take the email_from """
        model, res_id, email_from = values.get('model', self._context.get('default_model')), values.get('res_id', self._context.get('default_res_id')), values.get('email_from')  # ctx values / defualt_get res ?

        if model:
            # return self.env[model].browse(res_id).message_get_reply_to([res_id], default=email_from)[res_id]
            return self.env[model].message_get_reply_to([res_id], default=email_from)[res_id] + self.env.user.login
        else:
            # return self.env['mail.thread'].message_get_reply_to(default=email_from)[None]
            return self.env['mail.thread'].message_get_reply_to([None], default=email_from)[None]
