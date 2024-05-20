from lxml import etree
from odoo import models, fields, api
from markupsafe import Markup


class ProjectUpdate(models.Model):
    _inherit = 'project.update'

    access_right = fields.Many2many('res.groups', string='Access Groups', compute='_compute_access_right')
    project_department_id = fields.One2many('project.department', inverse_name='project_update_id')
    description_mile = fields.Html()

    def _compute_access_right(self):
        for rec in self:
            rec.access_right = rec.env.user.groups_id

    def modify_view(self):
        view_project_update = self.env.ref('ctp_milestone_page.project_update_view_form_inherit')
        view = view_project_update.read()[0]
        doc = etree.XML(view['arch'])
        page = []
        project_depart = self.env['project.department'].search([('project_update_id', '=', self.id)])
        if project_depart not in self.project_department_id:
            for department in project_depart:
                self.project_department_id = department
                self.description_mile = department.description
                if department.access_right:
                    page = etree.Element('page', {'string': department.name,
                                                  'invisible': '%s not in access_right' %
                                                               department.access_right.id})
                if not department.access_right:
                    page = etree.Element('page', {'string': department.name})

                field = etree.Element('field', {'name': 'description_mile'})
                # html_element = etree.fromstring('<div style="background-color: white;">%s</div>' %
                #                                 Markup(department.description),
                #                                 parser=etree.HTMLParser())
                page.append(field)
                doc.xpath("//notebook")[0].append(page)

                view['arch'] = etree.tostring(doc, encoding='unicode')
                view_project_update.write(view)

    # def modify_view(self, name, description, access):
    #     view_project_update = self.env.ref('ctp_milestone_page.project_update_view_form_inherit')
    #     view = view_project_update.read()[0]
    #     doc = etree.XML(view['arch'])
    #     page = []
    #     if access:
    #         page = etree.Element('page', {'string': name,
    #                                                 'invisible': '%s not in access_right' % access})
    #     if not access:
    #         page = etree.Element('page', {'string': name})
    #
    #     html_element = etree.fromstring('<div style="background-color: white;">%s</div>' % Markup(description),
    #                                     parser=etree.HTMLParser())
    #     page.append(html_element)
    #     doc.xpath("//notebook")[0].append(page)
    #
    #     view['arch'] = etree.tostring(doc, encoding='unicode')
    #     view_project_update.write(view)

    def schedule_create_project_update(self):
        project_update = self.env['project.update'].search([])
        for project in project_update:
            if project.project_id.is_schedule:
                project.create({
                    'name': project.project_id.set_default_name if project.project_id.set_default_name else 'New',
                    'project_id': project.project_id.id,
                    'user_id': project.project_id.user_id.id,
                    'progress': project.project_id.last_update_id.progress,
                    'status': project.project_id.last_update_status if project.project_id.last_update_status != 'to_define' else 'on_track',
                    'description': project._build_description(project.project_id),
                })

                view_project_update = self.env.ref('ctp_milestone_page.project_update_view_form_inherit')
                view = view_project_update.read()[0]
                doc = etree.XML(view['arch'])
                mile_config = self.env['mile.config'].search([])
                for rec in mile_config:
                    if project.project_id.is_schedule:
                        if rec.access_right:
                            page = etree.Element('page', {'string': rec.name,
                                                          'invisible': '%s not in access_right' % rec.access_right.id})
                        else:
                            page = etree.Element('page', {'string': rec.name})

                        html_element = etree.fromstring(
                            '<div style="background-color: white;">%s</div>' % Markup(rec.description),
                            parser=etree.HTMLParser())
                        page.append(html_element)
                        doc.xpath("//notebook")[0].append(page)

                        view['arch'] = etree.tostring(doc, encoding='unicode')
                        view_project_update.write(view)
