# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Climbing Gym',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Climbing Gym',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/gym_views.xml',
        'views/equipment_views.xml',
        'views/client_views.xml',
        'views/visits_views.xml',
        'views/ticket_views.xml',
        'views/service_views.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
