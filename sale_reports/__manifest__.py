# noinspection PyStatementEffect
{
    'name': 'Sale reports',
    'version': '1.0.0',
    'author': 'NumDesk',
    'category': 'Reports',
    'summary': 'Product/Summary Sale Reports',
    'description': """Product/Summary Sale Reports""",
    'depends': ['base', 'account'],
    #'sale', 'product', 'purchase', 'report_xlsx',
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_view_wizard.xml',
        'wizard/invoice_view_wizard.xml',
        'report/report.xml',
        'views/templates.xml',
        'views/views.xml',
    ],
    'application': False,
    'installable': True,
    'license': 'LGPL-3',
}
