{
    'name': "Product Variant",
    'summary': """,
    'description': """,
    'author': "Amitkumar",

    'depends': ['base','web','product'],

    'data': [
        'security/ir.model.access.csv',
        'views/product_variant_view.xml',
        'views/part_lines_view.xml',
    ],

    'license':'LGPL-3',

    'installable': True,
    'auto_install': True,
    'application': True,
}