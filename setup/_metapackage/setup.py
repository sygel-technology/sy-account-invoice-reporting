import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-account-invoice-reporting",
    description="Meta package for sygel-technology-sy-account-invoice-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-delete_payment_reference_invoice_report>=15.0dev,<15.1dev',
        'odoo-addon-invoice_report_hide_price>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
