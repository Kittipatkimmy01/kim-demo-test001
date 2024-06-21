from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    name_ch = fields.Char()
    recruitment_id = fields.Many2one('hr.applicant', string='Related Recruitment')
    recruitment_name = fields.Char(compute='_compute_recruitment_name')

    @api.depends('recruitment_id')
    def _compute_recruitment_name(self):
        for rec in self:
            if rec.recruitment_id:
                rec.recruitment_name = rec.recruitment_id.name
            else:
                rec.recruitment_name = ''

    def action_open_recruitment(self):
        self.ensure_one()
        action = {
            'res_model': 'hr.applicant',
            'type': 'ir.actions.act_window',
        }
        if self.recruitment_id:
            action.update({
                'view_mode': 'form',
                'res_id': self.recruitment_id.id,
            })

        return action
