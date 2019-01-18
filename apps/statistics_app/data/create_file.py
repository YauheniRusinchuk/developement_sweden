import csv


fieldList = ['Username', 'Notes_count', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday'
]


with open('statistics.csv', 'w') as file:
    create = csv.DictWriter(file, fieldnames=fieldList)

    create.writeheader()
    create.writerow({
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
