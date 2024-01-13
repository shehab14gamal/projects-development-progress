from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    github_account = fields.Char(string='Github Account', )
    collaborators_ids = fields.One2many('collaborator.collaborator', 'employee_id')

    @api.constrains('active')
    def check_active_projects_for_employee(self):

        """a function that triggers a warning msg while archiving an employee
         that is active collaborator in some project
          """
        for rec in self:
            if rec.active == False:
                """
                this syntax is valid also:
                  active_projects = rec.env['collaborator.collaborator'].search_count(
                    [('status', '=', 'active'), ('employee_id', '=', rec.id)])
                """
                active_projects = len(rec.collaborators_ids.filtered(lambda c: c.status =='active'))
                if active_projects and active_projects != 0:
                    raise ValidationError(
                        'Sorry ! you can not archive an employee who is collaborator in an active project !')
