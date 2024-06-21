from odoo import models, fields


class Applicant(models.Model):
    _inherit = "hr.applicant"

    name_ch = fields.Char()

    def _get_employee_create_vals(self):
        self.ensure_one()
        res = super(Applicant, self)._get_employee_create_vals()
        if 'name_ch' not in res:
            res.update({
                'name_ch': self.name_ch if self.name_ch else '',
                'recruitment_id': self.id,
            })

        return res
