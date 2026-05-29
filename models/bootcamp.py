from odoo import models, fields

class SkillBootcamp(models.Model):
    _name = 'skill.bootcamp'
    _description = 'Bootcamp / Course'
    _rec_name = 'name'

    name = fields.Char(required=True)
    code = fields.Char()
    description = fields.Text()
    duration_days = fields.Integer()
    category = fields.Selection([
        ('tech', 'Technology'),
        ('business', 'Business'),
        ('design', 'Design'),
    ])
    active = fields.Boolean(default=True)
    batch_ids = fields.One2many('skill.batch', 'bootcamp_id')