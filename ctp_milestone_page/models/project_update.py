from lxml import etree, html
from odoo import models, fields, api
from markupsafe import Markup


class ProjectUpdate(models.Model):
    _inherit = 'project.update'

    access_right = fields.Many2many('res.groups', string='Access Groups', compute='_compute_access_right')

    def _compute_access_right(self):
        for rec in self:
            rec.access_right = rec.env.user.groups_id

    def modify_view(self, name, description, access):
        view_project_update = self.env.ref('ctp_milestone_page.project_update_view_form_inherit')
        view = view_project_update.read()[0]
        doc = etree.XML(view['arch'])
        if access:
            groups = self.env.user.groups_id
            access_group = groups.filtered(lambda group: group.id == access)
            page = etree.Element('page', {'string': name,
                                                    'invisible': '%s not in access_right' % access_group.id})
        if not access:
            page = etree.Element('page', {'string': name})

        if not doc.xpath("//notebook/page[@string='%s']" % name):
            html_element = etree.fromstring('<div style="background-color: white;">%s</div>' % Markup(description),
                                                parser=etree.HTMLParser())
            page.append(html_element)
            doc.xpath("//notebook")[0].append(page)

            view['arch'] = etree.tostring(doc, encoding='unicode')
            view_project_update.write(view)
