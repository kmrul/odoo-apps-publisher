from odoo import fields, models, api


class WhatsappMessageWizard(models.Model):
    _name = 'whatsapp.message.wizard'

    user_id = fields.Many2one('res.partner', string='Recipients')
    mobile_number = fields.Char(related='user_id.mobile', required=True)
    message = fields.Text(string="Message")

    def send_message_whatsapp(self):
        if self.message and self.mobile_number:
            msg_string = ''
            message = self.message.split(' ')
            if not message:
                message = 'Hello I am test'
            for msg in message:
                msg_string = msg_string + msg + '%20'
            msg_string = msg_string[:(len(msg_string) - 3)]
            number = self.user_id.mobile
            link = "https://web.whatsapp.com/send?phone=" + number
            send_msg = {
                'type': 'ir.actions.act_url',
                'url': link + "&text=" + msg_string,
                'target': 'new',
                'res_id': self.id
            }

            return send_msg
