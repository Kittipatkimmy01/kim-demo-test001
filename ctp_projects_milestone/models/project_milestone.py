from odoo import _, api, fields, models
from lxml import etree

class ProjectMilestone(models.Model):
    _inherit = 'project.milestone'

    responsible_id = fields.Many2one('res.users', string='Responsible', tracking=True)
    start_date = fields.Date(string='Start Date', store=True, tracking=True, copy=False)
    is_manager = fields.Boolean(compute='_compute_is_manager', invisible=True)

    @api.depends('responsible_id')
    def _compute_is_manager(self):
        for rec in self:
            if rec.env.user.has_group('project.group_project_manager'):
                rec.is_manager = True
            else:
                rec.is_manager = False
    # @api.model
    # def fields_get(self, allfields=None, attributes=None):
    #     res = super().fields_get(allfields, attributes)
    #     if not self.env.user.has_group('project.group_project_manager'):
    #         res['responsible_id']['readonly'] = True
        #     res['responsible_id']['readonly'] = True
        #     res['start_date']['readonly'] = True
        #     res['deadline']['readonly'] = True
            # if self.responsible_id:
            #     res['responsible_id']['readonly'] = True
            # if self.start_date:
            #     res['start_date']['readonly'] = True
            # if self.deadline:
            #     res['deadline']['readonly'] = True
        # return res

    # @api.model
    # def fields_get(self, allfields=None, attributes=None):
    #     res = super().fields_get(allfields, attributes)
    #     if not self._context.get('from_ui', False):
    #         if not self.env.user.has_group('project.group_project_manager'):
    #             if 'responsible_id' in res and not self._context.get('from_ui', False) and self.responsible_id:
    #                 res['responsible_id']['readonly'] = True
    #             if 'start_date' in res and not self._context.get('from_ui', False) and self.start_date:
    #                 res['start_date']['readonly'] = True
    #             if 'deadline' in res and not self._context.get('from_ui', False) and self.deadline:
    #                 res['deadline']['readonly'] = True
    #     return res