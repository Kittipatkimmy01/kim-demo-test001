from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    associate_id = fields.Many2one('res.partner', string='Associate')
    count_associate = fields.Integer(compute='_compute_count_associate')
    associate_ids = fields.Many2many(comodel_name='res.partner', compute='_compute_associate_ids')

    @api.depends('associate_id')
    def _compute_associate_ids(self):
        for rec in self:
            associate_list = []
            if rec.associate_id:
                associate = self.search([('associate_id', '=', rec.associate_id.id)])
                for record in associate:
                    if record.id not in associate_list:
                        associate_list.append(record.id)

                rec.associate_ids = [(6, 0, associate_list)]
            else:
                rec.associate_ids = [(5, 0, 0)]

    @api.depends('associate_ids')
    def _compute_count_associate(self):
        for rec in self:
            count = 0
            associate = rec.associate_ids
            count += len(associate.ids) if associate else 0

            rec.count_associate = count

    def action_view_associate(self):
        self.ensure_one()
        action = {
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
        }
        if self.count_associate == 1:
            action.update({
                'view_mode': 'form',
                'res_id': self.id,
            })
        else:
            action.update({
                'name': _("Associate generated from %s", self.name),
                'domain': [('id', 'in', self.associate_ids.ids)],
                'view_mode': 'tree,form',
            })

        return action
