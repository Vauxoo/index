# Copyright 2021 Vauxoo
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Instance Creator',
    'summary': '''
    Instance creator for index. This is the app.
    ''',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'LGPL-3',
    'category': 'Installer',
    'version': '14.0.1.0.0',
    'depends': [
        'sale_management',
        'crm',
        'stock',
        'account_accountant',
        'purchase',
        'hr_expense',
        'sale_subscription',
        'contacts',
        'l10n_mx_edi_landing',
        'l10n_mx_reports_closing',
        'l10n_mx',
        'l10n_mx_edi',
        'l10n_mx_avoid_reversal_entry',
    ],
    'test': [
    ],
    'data': [
        'data/res_company_data.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
