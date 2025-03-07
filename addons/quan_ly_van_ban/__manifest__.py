# -*- coding: utf-8 -*-
{
    'name': "quan_ly_van_ban",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Quan ly van ban 
    """,

    'author': "Nhom 2 - CNTT 1504",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nhan_su'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/van_ban_di.xml',
        'views/trang_thai.xml',
        'views/do_mat.xml',
        'views/loai_van_ban.xml',
        'views/van_ban_den.xml',
        'views/nam.xml',
        'views/cong_viec.xml',
        'views/ho_so.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
