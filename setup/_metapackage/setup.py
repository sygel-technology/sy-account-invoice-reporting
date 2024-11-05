import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-account-invoice-reporting",
    description="Meta package for sygel-technology-sy-account-invoice-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_invoice_report_grouped_by_picking_hide_pickings>=16.0dev,<16.1dev',
        'odoo-addon-delete_payment_reference_invoice_report>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
