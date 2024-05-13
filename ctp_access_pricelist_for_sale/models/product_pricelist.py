from odoo import fields, models, _


class Pricelist(models.Model):
    _inherit = "product.pricelist"

    group_access_id = fields.Many2one('res.groups', string='Group Sale', domain="[('category_id.name', '=', 'Sales')]")
