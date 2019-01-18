import csv


fieldList = ['Id','Username', 'Notes_count', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday'
]


with open('statistics.csv', 'w') as file:
    create = csv.DictWriter(file, fieldnames=fieldList)

    create.writeheader()
    create.writerow({
        'Id': '1',
        'Username': 'REM',
        'Notes_count': '21',
        'Monday': '0',
        'Tuesday': '2',
        'Wednesday': '5',
        'Thursday': '0',
        'Friday': '10',
        'Saturday': '2',
        'Sunday': '2',
    })

    create.writerow({
        'Id': '2',
        'Username': 'Bill',
        'Notes_count': '0',
        'Monday': '0',
        'Tuesday': '0',
        'Wednesday': '0',
        'Thursday': '0',
        'Friday': '0',
        'Saturday': '0',
        'Sunday': '0',
    })
