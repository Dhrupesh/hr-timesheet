# Copyright 2018 Brainbean Apps
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Task Logs Analysis',
    'version': '12.0.1.0.0',
    'category': 'Human Resources',
    'website': 'https://github.com/OCA/hr-timesheet',
    'author':
        'Brainbean Apps, '
        'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'summary': 'Analyze tracked time in Pivot, Graph views',
    'depends': [
        'hr_timesheet',
    ],
    'data': [
        'views/account_analytic_line.xml',
    ],
}
