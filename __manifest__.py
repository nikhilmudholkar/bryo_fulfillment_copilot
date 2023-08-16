{
    'name': 'Bryo fulfillment copilot',
    'version': '1.0',
    'category': 'Extra Tools',
    'sequence': '-100',
    'description': """Fulfillment copilot for testing for Bryo UG""",
    'author': 'Bryo UG',
    'maintainer': 'Bryo UG',
    'license': 'LGPL-3',
    'website': 'https://www.bryo.io',
    'summary': 'Odoo 16 developement test module',
    'data': [
        'security/ir.model.access.csv',
        # 'views/menu.xml',
        # 'views/sales_order.xml',
        'views/order_tracking_menu.xml',
        'views/sale_order_table.xml',
        # 'views/orders_table_1.xml',
        # 'views/ordered_products.xml',
        # 'views/stock_levels.xml',
        # 'views/fulfillment.xml',
        # 'views/stock_movements.xml',
        # 'views/ai_copilot.xml',
        'views/ai_copilot.xml',
        'data/custom_channels.xml',
    ],
    "depends": [
        "sale",
    ]
}