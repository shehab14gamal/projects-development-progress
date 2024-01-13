# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Projects Development Progress',
    'version': '1.0',
    'summary': 'Projects Development Progress',
    'description': """
Projects Development Progress
====================
used to track its projects' development progress with the clients    """,
    'category': 'Management',
    'depends': ['hr', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_project_form_view_inherit.xml',
        'views/hr_employee_views.xml',
        'reports/project_report.xml',

    ],
    'assets': {

        'web.assets_backend': ['projects_development_progress/static/src/css/style.css'],

    }
}
