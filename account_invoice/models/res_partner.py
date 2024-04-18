from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    pnd_branch = fields.Char()
    pnd_address = fields.Char()
    pnd_room_number = fields.Char()
    pnd_floor = fields.Char()
    pnd_village = fields.Char()
    pnd_address_number = fields.Char()
    village_village = fields.Char()
    alley_alley = fields.Char()
    pnd_street = fields.Char()
    pnd_district = fields.Char()
    pnd_district2 = fields.Char()
    pnd_province_province = fields.Char()
    pnd_zip_code = fields.Char()
    use_pnd_address = fields.Boolean(default=False)

    # branch = fields.Char()
