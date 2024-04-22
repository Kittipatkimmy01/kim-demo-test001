from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    branch = fields.Char()
    re_branch = fields.Char(compute='_compute_research_branch')

    @api.onchange('branch')
    def _compute_research_branch(self):
        for rec in self:
            if rec.parent_id:
                rec.branch = rec.parent_id.branch

            code = rec.branch
            if isinstance(code, str) and code.isdigit() and int(code) >= 1:
                rec.re_branch = f"{code}"
            elif rec.branch == 'สำนักงานใหญ่' or rec.branch == 'Head Office' or not rec.branch or rec.branch == '00000':
                rec.re_branch = '00000'
            elif rec.branch and any(c.isalpha() for c in rec.branch):
                rec.re_branch = ''.join(['0' if c.isalpha() else c for c in rec.branch])
