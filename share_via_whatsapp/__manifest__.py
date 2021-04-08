{
    'name': 'Share via Whatsapp',
    'version': '13.0.0.1',
    'summary': 'Share customer, sale, crm etc via whatsapp',
    'author': 'Kamrul Hasan',
    'company': 'BYSL',
    'category': 'connector',
    'sequence': 4,
    'depends': [
      'base', 'contacts', 'crm', 'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/whatsapp_button_integration_views.xml',
        'wizard/whatsapp_wizard.xml'
    ],
    'demo':[

    ],
    'qweb':[

    ],
    'installable': True,
    'application': True,
    'auto_install': False

}