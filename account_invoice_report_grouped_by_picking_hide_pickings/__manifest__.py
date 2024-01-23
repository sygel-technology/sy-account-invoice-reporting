# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Account Invoice Report Grouped By Picking Hide Pickings',
    'summary': 'Hide pickings on the account invoice report grouped by pickings',
    'version': '16.0.1.0.0',
    'category': 'Accounting & Finance',
    'website': 'https://sygel.es',
    'author': 'Sygel, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'account_invoice_report_grouped_by_picking',
    ],
    'data': [
        'views/stock_picking_views.xml',
        'wizards/stock_picking_return_views.xml'
    ],
}
