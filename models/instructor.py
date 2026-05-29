from odoo import models, fields

class SkillInstructor(models.Model):
    _name = 'skill.instructor'
    _description = 'Instructor'
    _rec_name = 'name'

    name = fields.Char(required=True)
    instructor_code = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    bio = fields.Text()
    user_id = fields.Many2one('res.users', string='User Account')
    active = fields.Boolean(default=True)
    session_ids = fields.One2many('skill.session', 'instructor_id')