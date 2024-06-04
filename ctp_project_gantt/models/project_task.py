from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    respon_user_id = fields.Many2one('res.users', string='Responsible')
    color_by_department = fields.Integer(related='respon_user_id.department_id.color')
