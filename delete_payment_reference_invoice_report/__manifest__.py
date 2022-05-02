# Copyright 2022 Angel Garcia de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Delete payment reference from invoice reports",
    "summary": "Delete payment reference from invoice reports",
    "version": "14.0.1.0.0",
    "category": "Custom",
    "website": "https://www.sygel.es",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'base',
        'web',
    ],
    "data": [
        "report/report_invoice.xml",
    ],
}
