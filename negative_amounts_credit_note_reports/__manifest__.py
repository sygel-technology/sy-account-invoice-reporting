# Copyright 2022 Angel Garcia de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Negative amounts in credit note reports",
    "summary": "Show negative amounts in Credit Note reports.",
    "version": "14.0.1.0.0",
    "category": "Accounting",
    "website": "https://www.sygel.es",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'account',
    ],
    "data": [
        "report/report_invoice.xml",
        "views/res_config_settings_view.xml",
    ],
}
