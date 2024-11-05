import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-sygel-technology-sy-account-invoice-reporting",
    description="Meta package for sygel-technology-sy-account-invoice-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-delete_payment_reference_invoice_report',
        'odoo14-addon-negative_amounts_credit_note_reports',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
