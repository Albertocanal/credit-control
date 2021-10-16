import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-credit-control",
    description="Meta package for oca-credit-control Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-account_financial_risk',
        'odoo11-addon-account_payment_return_financial_risk',
        'odoo11-addon-partner_risk_insurance',
        'odoo11-addon-sale_financial_risk',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
