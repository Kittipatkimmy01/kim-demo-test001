from odoo import models, fields, api


class MilestoneConfig(models.Model):
    _name = 'mile.config'
    _order = 'sequence ASC'

    name = fields.Char('Name')
    sequence = fields.Integer(default=50)
    description = fields.Html(string='Description', translate=True)
    access_right = fields.Many2one('res.groups', string='Access Groups')

    @api.model_create_single
    def create(self, vals):
        res = super(MilestoneConfig, self).create(vals)
        name = vals.get('name')
        description = vals.get('description')
        access = vals.get('access_right')
        project_update = self.env['project.update'].search([])
        for update in project_update:
            if update:
                self.env['project.department'].create({
                    'name': name,
                    'description': description,
                    'access_right': access,
                    'project_update_id': update.id,
                })
        return res
