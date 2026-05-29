from odoo import models, fields

class SkillBatch(models.Model):
    _name = 'skill.batch'
    _description = 'Training Batch'
    _rec_name = 'name'

    name = fields.Char(required=True)
    bootcamp_id = fields.Many2one('skill.bootcamp', required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    capacity = fields.Integer()
    instructor_ids = fields.Many2many('skill.instructor')
    student_ids = fields.Many2many('skill.student')
    session_ids = fields.One2many('skill.session', 'batch_id')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ], default='draft')