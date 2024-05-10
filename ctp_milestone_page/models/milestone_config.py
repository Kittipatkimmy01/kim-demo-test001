from odoo import models, fields, api


class MilestoneConfig(models.Model):
    _name = 'mile.config'
    _order = 'sequence ASC'

    name = fields.Char('Name')
    sequence = fields.Integer(default=50)
    description = fields.Html(string='Description', translate=True)
    access_right = fields.Many2one('res.groups', string='Access Groups')
    is_schedule = fields.Boolean(default=False, string='Set Schedule')

    @api.model_create_single
    def create(self, vals):
        res = super(MilestoneConfig, self).create(vals)
        name = vals.get('name')
        description = vals.get('description')
        access = vals.get('access_right')
        self.env['project.update'].modify_view(name, description, access)
        return res
