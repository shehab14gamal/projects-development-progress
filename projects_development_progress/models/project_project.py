from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class ProjectProject(models.Model):
    _inherit = 'project.project'

    odoo_version = fields.Integer(string='Odoo Version')
    odoo_type = fields.Selection([
        ('community','Community'),
        ('enterprise','Enterprise')
    ],default='enterprise',string='Odoo type')
    github_repo_name = fields.Char(string='Github Repo Name')
    github_repo_url = fields.Char(string='Github Repo Url',widget='url')
    hosting = fields.Selection([
        ('on_prem','on Prem'),
        ('cloud_hosting','Cloud Hosting'),
        ('odoo_sh','Odoo SH'),
        ('odoo_online','Odoo Online')
    ],default='on_prem',string='Hosting')
    hosting_description = fields.Text(string='Hosting Description')
    collaborators_ids = fields.One2many('collaborator.collaborator','project_id')


