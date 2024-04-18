from odoo import models, fields


class AccountPND1G(models.Model):
    _name = 'account.pnd1g'

    name = fields.Char('No.', size=32, required=True)
    company_id = fields.Many2one(
        'res.company',
        'Company',
        required=True,
        default=lambda self: self.env.company.id,
    )
    partner_id = fields.Many2one('res.partner')
    normal_confirm = fields.Boolean(default=False)
    further_confirm = fields.Boolean(default=False)
    further_time = fields.Char()
    vat_year = fields.Char()
    attachment = fields.Boolean(default=False)
    attachment_qty = fields.Char()
    recording = fields.Boolean(default=False)
    recording_qty = fields.Char()
    register_number = fields.Char()
    register_ref = fields.Char()
    # สรุปรายการภาษีที่นำาส่ง
    general_wages_qty = fields.Char()
    general_total_income = fields.Float()
    general_vat = fields.Float()
    according = fields.Char()
    according_date = fields.Date()
    according_qty = fields.Char()
    according_total_income = fields.Float()
    according_vat = fields.Float()
    one_time_qty = fields.Char()
    one_time_total_income = fields.Float()
    one_time_vat = fields.Float()
    in_country_qty = fields.Char()
    in_country_total_income = fields.Float()
    in_country_vat = fields.Float()
    out_country_qty = fields.Char()
    out_country_total_income = fields.Float()
    out_country_vat = fields.Float()
    sum_qty = fields.Char()
    sum_total_income = fields.Float()
    sum_vat = fields.Float()

    submit_date = fields.Date()

    def action_print_pnd1g(self):
        return self.env.ref('account_invoice.account_pnd1g_report_action').report_action(self)
