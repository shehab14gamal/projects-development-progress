from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
import json


class Controller(http.Controller):

    @http.route('/employees-active-projects', auth='user', type='http', methods=['GET'])
    def get_employees_with_active_projects(self):
        """a controller to get all employee with their active projects
             with the following attributes:
             Rest API,
             Method GET,
             Authentication: Basic,
             Input: nothing,
             Response, JSON
          """

        employees = request.env['hr.employee'].sudo().search([])

        result = []
        for employee in employees:
            active_projects = employee.collaborators_ids.filtered(lambda c: c.status == 'active')
            if active_projects:
                result.append({
                    'id': employee.id,
                    'name': employee.name,
                    'active_projects': [{'id': collaborator.project_id.id, 'name': collaborator.project_id.name} for
                                        collaborator in active_projects]
                })

        return request.make_response(
            headers=[('Content-Type', 'application/json')],
            data=json.dumps(result, indent=2)
        )
