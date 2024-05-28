from odoo import models, fields, api


class HRExpense(models.Model):
    _inherit = 'hr.expense'

    analytic_distribution_ids = fields.Many2many('account.analytic.account',
                                                 compute="_compute_analytic_distribution_ids", readonly=False, store=True,
                                                 string='Analytic Distribution Project')

    @api.onchange('analytic_distribution')
    @api.depends('analytic_distribution')
    def _compute_analytic_distribution_ids(self):
        for rec in self:
            if rec.analytic_distribution:
                dist_key = list(rec.analytic_distribution.keys())
                int_keys = []
                for key in dist_key:
                    split_keys = key.split(',')
                    for split_key in split_keys:
                        try:
                            int_keys.append(int(split_key))
                        except ValueError:
                            continue  # Skip any non integer values

                if int_keys:
                    get_analytic = self.env['account.analytic.account'].search([('id', 'in', int_keys), '|',
                                                                                ('plan_id.name', '=', 'Projects'),
                                                                                ('plan_id.name', '=', 'Internal')])
                    rec.analytic_distribution_ids = get_analytic
                else:
                    rec.analytic_distribution_ids = False
            else:
                rec.analytic_distribution_ids = False
                