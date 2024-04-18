from odoo import models, fields, api


class AccountPP30(models.Model):
    _name = "account.pp30"

    name = fields.Char('No.', size=32, required=True)
    date_doc = fields.Date('Document Date', default=fields.Datetime.now)
    company_id = fields.Many2one(
        'res.company',
        'Company',
        required=True,
        default=lambda self: self.env.company.id,
    )
    partner_id = fields.Many2one('res.partner', 'Partner', required=False)
    account_id = fields.Many2one('account.account', 'Account', required=False)
    date_pnd = fields.Date('Date', required=True, default=fields.Datetime.now)
    base_amount = fields.Float(digits="Product Price", string='Base Amount')
    sale_amount = fields.Boolean('ยอดขายแจ้งไว้ขาด', default='')
    purchase_amount = fields.Boolean('ยอดซื้อแจ้งไว้เกิน', default='')
    sale_month = fields.Float()
    sale_tax_rate = fields.Float()
    taxable_sale = fields.Float()
    exempted_sales = fields.Float()
    sale_tax_month = fields.Float()
    sale_vat_amount = fields.Boolean('ยอดขายแจ้งไว้เกิน', default='')
    purchase_vat_amount = fields.Boolean('ยอดซื้อแจ้งไว้ขาด', default='')
    purchase_tax_amount = fields.Float()
    purchase_tax_month = fields.Float()
    tax_due_month = fields.Float()
    tax_paid_month = fields.Float()
    tax_paid_access = fields.Float()
    net_tax_paid = fields.Boolean('ต้องชำระ (ถ้า 8. มากกว่า 10.)', default='')
    tax_paid = fields.Float()
    net_tax_over_paid = fields.Boolean('ชำระเกิน ((ถ้า 10. มากกว่า 8.) หรือ (9. รวมกับ 10.))', default='')
    tax_over_paid = fields.Float()
    document_item = fields.Boolean(default='')
    head_company = fields.Boolean(default='')
    branch = fields.Boolean(default='')
    branch_code = fields.Char('')
    documents_together = fields.Boolean(default='')
    head_company_to = fields.Boolean(default='')
    branch_to = fields.Boolean(default='')
    branch_code_to = fields.Char('')
    normal_confirm = fields.Boolean(default='')
    further_confirm = fields.Boolean(default='')
    further_time = fields.Char()
    dead_line = fields.Boolean(default='')
    over_due = fields.Boolean(default='')
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
    #กรณียื่นเพิ่มเติม
    extra_money = fields.Float()
    fine = fields.Float()
    total_extra_money = fields.Float()
    total_fine = fields.Float()

    submit_date = fields.Date()

    def action_print_pnd30(self):
        return self.env.ref('account_invoice.account_pnd30_report_action').report_action(self)