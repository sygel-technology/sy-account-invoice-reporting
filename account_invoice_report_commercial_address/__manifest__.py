# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Invoice Report Commercial Address",
    "summary": "Add commercial address to invoice report",
    "version": "18.0.1.0.1",
    "license": "AGPL-3",
    "author": "Sygel",
    "category": "Accounting & Finance",
    "website": "https://github.com/sygel-technology/sy-account-invoice-reporting",
    "depends": [
        "account",
        "base",
    ],
    "data": [
        "views/account_move_views.xml",
        "reports/report_invoice.xml",
    ],
}
