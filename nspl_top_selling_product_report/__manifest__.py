{
    'name': 'Top and Least Selling Product Report',
    'version': '18.0',
    'summary': """Generate insightful reports on top and least selling products directly from Odoo Sales. 
    Analyze product performance based on sales data to make informed inventory and marketing decisions.
    """,
    'description': """
    This module provides detailed reports on your best and worst selling products.
    
    ✔ Identify top-performing products based on sales quantity  
    ✔ Detect least-selling or slow-moving items  
    ✔ Make informed decisions for purchasing, stocking, and promotions  
    ✔ View reports through an easy-to-use wizard and formatted PDF  
    
    A must-have tool for sales teams, inventory managers, and business owners.
    """,
    'category': 'Sales',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com/',
    'license': 'AGPL-3',
    'price': 15.00,
    'currency': 'USD',
    'depends': ['sale_management', 'stock'],
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'data': [
        'security/ir.model.access.csv',
        'report/top_selling_reports.xml',
        'report/top_selling_report_templates.xml',
        'wizard/top_selling_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
