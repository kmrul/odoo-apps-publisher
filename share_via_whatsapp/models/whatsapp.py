from odoo import fields, models, api, _

class ResPartnerExtend(models.Model):
    _inherit = 'res.partner'

    def whatsapp_message_partner(self):
        print('print whatsappp')
        return {
            'type': 'ir.actions.act_window',
            'name': _('Send Whatsapp Message'),
            'res_model': 'whatsapp.message.wizard',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {'default_user_id': self.id}
        }
