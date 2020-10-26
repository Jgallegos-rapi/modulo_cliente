# -*- coding: utf-8 -*-
{
    'name': "Modulo modo de pago en sale order",

    'summary': """
    Siempre documentar el resumen o descripcion
      
    """,

    'description': """
    Siempre documentar el resumen o descripcion
    """,

    'author': "Jose Gallegos",
    'website': "http://www.josegallegos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/sale_order_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
