OK_FORMAT = True
test = {
    'name':
    'q2bii',
    'points':
    2,
    'suites': [{
        'cases': [{
            'code':
            ">>> result_2bii.DataFrame().iloc[5, 2] == 'Pirates of the Caribbean: On Stranger Tides'\nTrue",
            'hidden': False,
            'locked': False
        }, {
            'code':
            ">>> result_2bii.DataFrame()['budget'].iloc[:5].sum() == 1318000000.0\nTrue",
            'hidden': False,
            'locked': False
        }],
        'scored':
        True,
        'setup':
        '',
        'teardown':
        '',
        'type':
        'doctest'
    }]
}
