from odoo import models, fields


class ProjectDepartment(models.Model):
    _name = 'project.department'

    name = fields.Char('Name')
    description = fields.Html(string='Description', translate=True)
    access_right = fields.Many2one('res.groups', string='Access Groups')
    project_update_id = fields.Many2one('project.update', string='Project Update')
