# -*- coding: utf-8 -*-
{
    'name': "/home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6",

    'summary': """
        MOT and service station""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Olena Postnikova",
    'website': "https://www.a4.com.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
