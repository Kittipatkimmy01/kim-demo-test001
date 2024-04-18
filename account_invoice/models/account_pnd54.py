from odoo import models, fields


class AccountPND54(models.Model):
    _name = 'account.pnd54'

    name = fields.Char('No.', size=32, required=True)
    company_id = fields.Many2one(
        'res.company',
        'Company',
        required=True,
        default=lambda self: self.env.company.id,
    )
    partner_id = fields.Many2one('res.partner')
    #การจ่ายเงินได้ตามมาตรา 70 แห่งประมวลรัษฎากร
    payee_name = fields.Char()
    office_location = fields.Char()
    street = fields.Char()
    city = fields.Char()
    country_id = fields.Many2one(string="Country", comodel_name='res.country')
    #การนำส่งภาษี
    tax_deducted = fields.Boolean(default=False)
    tax_on_sale = fields.Boolean(default=False)
    normal_confirm = fields.Boolean(default=False)
    further_confirm = fields.Boolean(default=False)
    further_time = fields.Char()
    #1. ประเภทเงินได้ที่จ่าย
    fee = fields.Boolean(default=False)
    royalties = fields.Boolean(default=False)
    patent_royalties = fields.Boolean(default=False)
    other_royalties = fields.Boolean(default=False)
    interest = fields.Boolean(default=False)
    other_interest = fields.Boolean(default=False)
    dividend = fields.Boolean(default=False)
    other_income_bool = fields.Boolean(default=False)
    other_income = fields.Char()
    boat_rental_fees = fields.Boolean(default=False)
    other_rental_fees = fields.Boolean(default=False)
    income_independent_bool = fields.Boolean(default=False)
    income_independent = fields.Char()
    #2.การคำนวณภาษี
    income = fields.Float()
    tax_money = fields.Float()
    percentage = fields.Char()
    extra_money = fields.Float()
    total = fields.Float()
    deducted = fields.Boolean(default=False)
    issue_taxes = fields.Boolean(default=False)
    tax_date = fields.Date()
    currency_ex_ref = fields.Char()
    #การจำหน่ายเงินกำไรตามมาตรา 70 ทวิ แห่งประมวลรัษฎากร
    office_sold = fields.Char()
    number_address = fields.Char()
    street_address = fields.Char()
    city_address = fields.Char()
    country_country_id = fields.Many2one(string="Country", comodel_name='res.country')
    profit = fields.Float()
    remittance_tax = fields.Float()
    extra_moneys = fields.Float()
    total_money = fields.Float()
    date_70_tw = fields.Date()
    tw_number = fields.Char()

    submit_date = fields.Date()

    def action_print_pnd54(self):
        return self.env.ref('account_invoice.account_pnd54_report_action').report_action(self)
