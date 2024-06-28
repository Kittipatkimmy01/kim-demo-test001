from odoo import fields, models


class StudioApprovalRule(models.Model):
    _inherit = "studio.approval.rule"

    def delete_approval(self, res_id):
        self.ensure_one()
        record = self.env[self.sudo().model_name].browse(res_id)
        record.check_access_rights('write')
        record.check_access_rule('write')
        ruleSudo = self.sudo()
        existing_entry = self.env['studio.approval.entry'].search([
            ('model', '=', ruleSudo.model_name),
            ('method', '=', ruleSudo.method), ('action_id', '=', ruleSudo.action_id.id),
            ('res_id', '=', res_id), ('rule_id', '=', self.id)])
        if not existing_entry.cancel:
            existing_entry._notify_cancel_approval()

        return super().delete_approval(res_id)


class StudioApprovalEntry(models.Model):
    _inherit = 'studio.approval.entry'

    cancel = fields.Boolean(string='Cancel')

    def _notify_cancel_approval(self):
        for entry in self:
            if not entry.rule_id.model_id.is_mail_thread:
                continue
            record = self.env[entry.model].browse(entry.res_id)
            record.message_post_with_source(
                'ctp_cancel_lognote.notify_cancel_approval',
                render_values={
                    'user_name': entry.user_id.display_name,
                    'group_name': entry.group_id.display_name,
                    'cancel': True,
                    },
                subtype_xmlid='mail.mt_note',
            )
