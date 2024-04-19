from odoo import models, fields


class AccountPP30(models.Model):
    _name = 'account.pp36'

    name = fields.Char('No.', size=32, required=True)
    company_id = fields.Many2one(
        'res.company',
        'Company',
        required=True,
        default=lambda self: self.env.company.id,
    )
    partner_id = fields.Many2one('res.partner', 'Partner', required=False)
    normal_confirm = fields.Boolean(default=False)
    further_confirm = fields.Boolean(default=False)
    further_time = fields.Char()
    #มีหน้าที่นำส่งภาษีมูลค่าเพิ่มกรณี
    pay_purchase = fields.Boolean(default=False)
    product_transfer = fields.Boolean(default=False)
    property_auction = fields.Boolean(default=False)
    #จ่ายเงินค่าซื้อสินค้าหรือบริการจ่ายเงินค่าซื้อสินค้าหรือบริการ
    name_operator = fields.Char()
    address = fields.Char()
    address_number = fields.Char()
    street = fields.Char()
    state = fields.Char()
    city = fields.Char()
    country_id = fields.Many2one(string="Country", comodel_name='res.country')
    post_address = fields.Char()
    pay_date = fields.Date()
    currency_ex_ref = fields.Char()
    pay_the_price_bool = fields.Boolean(default=False)
    entrepreneur = fields.Boolean(default=False)
    abroad = fields.Boolean(default=False)
    other_other = fields.Char()
    #รับโอนสินค้าฯ
    name_person_transfer = fields.Char()
    tax_id = fields.Char()
    address_transfer = fields.Char()
    address_transfer_number = fields.Char()
    floor = fields.Char()
    swine = fields.Char()
    village_number = fields.Char()
    village = fields.Char()
    alley_alley = fields.Char()
    transfer_street = fields.Char()
    subdistrict = fields.Char()
    district = fields.Char()
    province = fields.Char()
    zip_code = fields.Char()
    tell = fields.Char()
    transfer_date = fields.Date()
    list_product = fields.Char()
    #ขายทอดตลาด
    operator_name = fields.Char()
    operator_tax_id = fields.Char()
    operator_address = fields.Char()
    operator_address_number = fields.Char()
    operator_floor = fields.Char()
    operator_swine = fields.Char()
    operator_village_number = fields.Char()
    operator_village = fields.Char()
    operator_alley_alley = fields.Char()
    operator_street = fields.Char()
    operator_subdistrict = fields.Char()
    operator_district = fields.Char()
    operator_province = fields.Char()
    operator_zip_code = fields.Char()
    operator_tell = fields.Char()
    operator_transfer_date = fields.Date()
    operator_list_product = fields.Char()
    #การคำนวณภาษี
    amount_paid = fields.Float()
    amount_vat = fields.Float()
    amount_ch = fields.Char()
    #กรณีนำส่งภาษีเกินกำหนดเวลา หรือไม่ถูกต้อง
    extra_money = fields.Float()
    find = fields.Float()
    total_vat = fields.Float()
    total_ch = fields.Char()

    pay_payment = fields.Char()
    submit_date = fields.Date()
    user_id = fields.Many2one('res.users', 'ลงชื่อผู้ประกอบการ')

    def action_print_pnd36(self):
        return self.env.ref('account_invoice.account_pnd36_report_action').report_action(self)