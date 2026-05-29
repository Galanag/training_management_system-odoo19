from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SkillSession(models.Model):
    _name = 'skill.session'
    _description = 'Training Session'
    _inherit = ['mail.thread']
    _order = 'start_datetime'

    name = fields.Char(required=True)
    batch_id = fields.Many2one('skill.batch', required=True)
    instructor_id = fields.Many2one('skill.instructor', required=True)
    start_datetime = fields.Datetime(required=True)
    end_datetime = fields.Datetime(required=True)
    room = fields.Char()
    notes = fields.Text()
    state = fields.Selection([
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='planned')

    @api.constrains('start_datetime', 'end_datetime')
    def _check_dates(self):
        for rec in self:
            if rec.end_datetime <= rec.start_datetime:
                raise ValidationError(_('End time must be after start time'))

    @api.model
    def _cron_send_session_reminders(self):
        """Send email reminders 1 hour before session start."""
        now = fields.Datetime.now()
        one_hour_later = now + timedelta(hours=1)
        sessions = self.search([
            ('start_datetime', '>=', now),
            ('start_datetime', '<=', one_hour_later),
            ('state', '=', 'planned'),
        ])
        for session in sessions:
            session._send_reminder()

    def _send_reminder(self):
        template = self.env.ref('skillbridge.email_template_session_reminder', raise_if_not_found=False)
        if template:
            template.send_mail(self.id, force_send=True)