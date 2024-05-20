from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    is_schedule = fields.Boolean(default=False, string='Set Schedule')
    set_default_name = fields.Char()
