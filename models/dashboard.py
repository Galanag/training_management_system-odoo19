from odoo import models, fields, api

class SkillDashboard(models.TransientModel):
    _name = 'skill.dashboard'
    _description = 'Dashboard Data'

    total_students = fields.Integer(compute='_compute_stats')
    total_instructors = fields.Integer(compute='_compute_stats')
    total_bootcamps = fields.Integer(compute='_compute_stats')
    ongoing_sessions = fields.Integer(compute='_compute_stats')

    @api.depends()
    def _compute_stats(self):
        for rec in self:
            rec.total_students = self.env['skill.student'].search_count([])
            rec.total_instructors = self.env['skill.instructor'].search_count([])
            rec.total_bootcamps = self.env['skill.bootcamp'].search_count([])
            rec.ongoing_sessions = self.env['skill.session'].search_count([('start_datetime', '>=', fields.Datetime.now()), ('state', '!=', 'done')])
