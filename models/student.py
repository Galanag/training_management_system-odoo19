from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SkillStudent(models.Model):
    _name = 'skill.student'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(required=True)
    student_id = fields.Char(string='Student ID', required=True, copy=False, readonly=True,
                             default=lambda self: self.env['ir.sequence'].next_by_code('skill.student'))
    email = fields.Char()
    phone = fields.Char()
    birth_date = fields.Date()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    active = fields.Boolean(default=True)
    batch_ids = fields.Many2many('skill.batch', string='Batches')
    assignment_ids = fields.One2many('skill.assignment', 'student_id')
    attendance_ids = fields.One2many('skill.attendance', 'student_id')
    partner_id = fields.Many2one('res.partner', string='Contact')
    user_id = fields.Many2one('res.users', string='Portal User', help='For student portal access')

    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            if rec.email and not '@' in rec.email:
                raise ValidationError(_('Invalid email'))

    def action_open_portal(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/my/student/%d' % self.id,
            'target': 'self',
        }
        