from odoo import models, fields

class SkillAssignment(models.Model):
    _name = 'skill.assignment'
    _description = 'Assignment'
    _inherit = ['mail.thread']

    name = fields.Char(required=True)
    student_id = fields.Many2one('skill.student', required=True)
    instructor_id = fields.Many2one('skill.instructor')
    due_date = fields.Date()
    description = fields.Text()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('graded', 'Graded'),
    ], default='draft')
    grade = fields.Float()