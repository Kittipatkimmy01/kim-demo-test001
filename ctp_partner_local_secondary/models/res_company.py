# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    local_name = fields.Char(related="partner_id.local_name", inverse="_inverse_field", store=True)
    local_street = fields.Char(related="partner_id.local_street", inverse="_inverse_field", store=True)
    local_street2 = fields.Char(related="partner_id.local_street2", inverse="_inverse_field", store=True)
    local_city = fields.Char(related="partner_id.local_city", inverse="_inverse_field", store=True)
    local_state = fields.Char(related="partner_id.local_state", inverse="_inverse_field", store=True)
    local_country = fields.Char(related="partner_id.local_country", inverse="_inverse_field", store=True)
    local_zip = fields.Char(related="zip")

    def _inverse_field(self):
        for company in self:
            company.partner_id.company_id = getattr(company, 'id')
            company.partner_id.local_name = company.local_name
            company.partner_id.local_street = company.local_street
            company.partner_id.local_street2 = company.local_street2
            company.partner_id.local_city = company.local_city
            company.partner_id.local_state = company.local_state
            company.partner_id.local_country = company.local_country