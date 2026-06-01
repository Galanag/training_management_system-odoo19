{
    'name': 'SkillBridge Training Management',
    'version': '1.0',
    'category': 'Education/Training',
    'summary': 'Complete training institute ERP with pro features',
    'description': """
        SkillBridge Training Management System
    """,
    'author': 'Galana G.',
    'depends': ['base', 'mail', 'contacts', 'hr', 'calendar', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/student_views.xml',
        'views/instructor_views.xml',
        'views/bootcamp_views.xml',
        'views/batch_views.xml',
        'views/session_views.xml',
        'views/assignment_views.xml',
        'views/attendance_views.xml',
        'views/dashboard_views.xml',
        'data/sequence.xml', 
        'views/dashboard_template.xml',
    ],
    'assets': {
    'web.assets_backend': [
        'training_ms/static/src/scss/skillbridge.scss',
    ],
},
    # 'assets': {   # COMMENTED OUT TO AVOID STYLE ERRORS
    #     'web.assets_backend': [
    #         'skillbridge/static/src/js/dashboard.js',
    #         'skillbridge/static/src/scss/style.scss',
    #     ],
    # },
    'installable': True,
    'application': True,
}