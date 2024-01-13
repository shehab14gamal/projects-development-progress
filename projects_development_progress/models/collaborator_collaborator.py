from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class CollaboratorCollaborator(models.Model):
    _name = 'collaborator.collaborator'

    employee_id = fields.Many2one('hr.employee', srting='Employee')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], default='inactive', string='Status')
    project_id = fields.Many2one('project.project')


    def button_activate(self):
        """
           a button to activate collaborator
        """
        for rec in self:
            rec.status = 'active'

    def button_deactivate(self):
        """
           a button to deactivate collaborator
        """
        for rec in self:
            rec.status = 'inactive'
