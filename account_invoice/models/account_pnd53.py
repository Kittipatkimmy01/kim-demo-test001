from odoo import models, fields


class AccountPND53(models.Model):
    _name = 'account.pnd53'

    name = fields.Char('No.', size=32, required=True)
    partner_id = fields.Many2one('res.partner')
    normal_confirm = fields.Boolean(default=False)
    further_confirm = fields.Boolean(default=False)
    further_time = fields.Char()
    year = fields.Char()
    month_selected = fields.Selection([('01', 'มกราคม'),
                                       ('02', 'กุมภาพันธ์'),
                                       ('03', 'มีนาคม'),
                                       ('04', 'เมษายน'),
                                       ('05', 'พฤษภาคม'),
                                       ('06', 'มิถุนายน'),
                                       ('07', 'กรกฎาคม'),
                                       ('08', 'สิงหาคม'),
                                       ('09', 'กันยายน'),
                                       ('10', 'ตุลาคม'),
                                       ('11', 'พฤศจิกายน'),
                                       ('12', 'ธันวาคม')])
    remit_tax = fields.Selection([('r1', 'มาตรา 3 เตรส'), ('r2', 'มาตรา 65 จัตวา'), ('r3', 'มาตรา 69 ทวิ')])
    attachment = fields.Boolean(default=False)
    attachment_qty = fields.Char()
    attachment_qty_qty = fields.Char()
    recording = fields.Boolean(default=False)
    recording_qty = fields.Char()
    recording_qty_qty = fields.Char()
    register_number = fields.Char()
    register_ref = fields.Char()
    total_money = fields.Float()
    total_tax = fields.Float()
    extra_money = fields.Float()
    total = fields.Float()

    submit_date = fields.Date()

    def action_print_pnd53(self):
        return self.env.ref('account_invoice.account_pnd53_report_action').report_action(self)