# -*- coding: utf-8 -*-
{
    'name': "alquiler",

    'summary': """
       Gestión de alquiler de coches""",

    'description': """
        Módulo de pruebas
    """,

    'author': "Angel",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/alquiler_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/alquiler_cliente_report.xml',
        'data/alquiler_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'aplication': True,
}
