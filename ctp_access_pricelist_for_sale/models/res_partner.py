from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    group_access_ids = fields.Many2many('res.groups', string='Group IDS', compute='_compute_group_access_ids')

    def _compute_group_access_ids(self):
        for rec in self:
            rec.group_access_ids = rec.env.user.groups_id.filtered(lambda g: g.category_id and g.category_id.name
                                                                                and 'Sales' in g.category_id.name)