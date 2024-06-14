from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    name_ch = fields.Char()
