from odoo import models, fields

class SkillAttendance(models.Model):
    _name = 'skill.attendance'
    _description = 'Student Attendance'
    _order = 'date desc'

    student_id = fields.Many2one('skill.student', required=True)
    session_id = fields.Many2one('skill.session')
    date = fields.Date(default=fields.Date.today)
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ], default='present')