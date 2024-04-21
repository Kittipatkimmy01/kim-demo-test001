from odoo import models, fields


class AccountPND1(models.Model):
    _name = 'account.attach.pnd1g'

    name = fields.Char('No.', size=32, required=True)
    partner_id = fields.Many2one('res.partner')
    money_type = fields.Selection([('01', '(1) เงินได้ตามมาตรา 40 (1) เงินเดือน ค่าจ้าง ฯลฯ กรณีทั่วไป '),
                                   ('02', '(2) เงินได้ตามมาตรา 40 (1) เงินเดือน ค่าจ้าง ฯลฯ กรณีได้รับอนุมัติจากกรมสรรพากรให้หักอัตราร้อยละ 3'),
                                   ('03', '(3) เงินได้ตามมาตรา 40 (1) (2) กรณีนายจ้างจ่ายให้ครั้งเดียวเพราะเหตุออกจากงาน'),
                                   ('04', '(4) เงินได้ตามมาตรา 40 (2) กรณีผู้รับเงินได้เป็นผู้อยู่ในประเทศไทย'),
                                   ('05', '(5) เงินได้ตามมาตรา 40 (2) กรณีผู้รับเงินได้มิได้เป็นผู้อยู่ในประเทศไทย')])
    sheet = fields.Char('แผ่นที่')
    sheet_quantity = fields.Char('ในจำนวน')
    no_1 = fields.Char('ลำดับที่')
    tax_01 = fields.Many2one('res.partner', 'เลขประจำตัวผู้เสียภาษีอากร')
    amount_income = fields.Float(string='จำนวนเงินได้ที่จ่ายทั้งปี')
    amount_tax = fields.Float(string='จำนวนเงินภาษีที่หักและนำส่งทั้งปี')
    condition = fields.Char('เงื่อนไข')

    no_2 = fields.Char('ลำดับที่')
    tax_02 = fields.Many2one('res.partner', 'เลขประจำตัวผู้เสียภาษีอากร')
    amount_income_02 = fields.Float(string='จำนวนเงินได้ที่จ่ายทั้งปี')
    amount_tax_02 = fields.Float(string='จำนวนเงินภาษีที่หักและนำส่งทั้งปี')
    condition_02 = fields.Char('เงื่อนไข')

    no_3 = fields.Char('ลำดับที่')
    tax_03 = fields.Many2one('res.partner', 'เลขประจำตัวผู้เสียภาษีอากร')
    amount_income_03 = fields.Float(string='จำนวนเงินได้ที่จ่ายทั้งปี')
    amount_tax_03 = fields.Float(string='จำนวนเงินภาษีที่หักและนำส่งทั้งปี')
    condition_03 = fields.Char('เงื่อนไข')

    no_4 = fields.Char('ลำดับที่')
    tax_04 = fields.Many2one('res.partner', 'เลขประจำตัวผู้เสียภาษีอากร')
    amount_income_04 = fields.Float(string='จำนวนเงินได้ที่จ่ายทั้งปี')
    amount_tax_04 = fields.Float(string='จำนวนเงินภาษีที่หักและนำส่งทั้งปี')
    condition_04 = fields.Char('เงื่อนไข')

    no_5 = fields.Char('ลำดับที่')
    tax_05 = fields.Many2one('res.partner', 'เลขประจำตัวผู้เสียภาษีอากร')
    amount_income_05 = fields.Float(string='จำนวนเงินได้ที่จ่ายทั้งปี')
    amount_tax_05 = fields.Float(string='จำนวนเงินภาษีที่หักและนำส่งทั้งปี')
    condition_05 = fields.Char('เงื่อนไข')

    no_6 = fields.Char('ลำดับที่')
    tax_06 = fields.Many2one('res.partner', 'เลขประจำตัวผู้เสียภาษีอากร')
    amount_income_06 = fields.Float(string='จำนวนเงินได้ที่จ่ายทั้งปี')
    amount_tax_06 = fields.Float(string='จำนวนเงินภาษีที่หักและนำส่งทั้งปี')
    condition_06 = fields.Char('เงื่อนไข')

    no_7 = fields.Char('ลำดับที่')
    tax_07 = fields.Many2one('res.partner', 'เลขประจำตัวผู้เสียภาษีอากร')
    amount_income_07 = fields.Float(string='จำนวนเงินได้ที่จ่ายทั้งปี')
    amount_tax_07 = fields.Float(string='จำนวนเงินภาษีที่หักและนำส่งทั้งปี')
    condition_07 = fields.Char('เงื่อนไข')

    submit_date = fields.Date(string='ยื่นวันที่')
    user_id = fields.Many2one('res.users', 'ลงชื่อผู้จ่ายเงิน')

    def action_print_attach_pnd1g(self):
        return self.env.ref('account_invoice.account_attach_pnd1g_report_action').report_action(self)