import csv
import os


fieldList = ['Id','Username', 'Notes_count', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday'
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path = os.path.join(BASE_DIR, 'data')


class StatisticsFile:

    def __init__(self):
        self._path = path + "/" + 'statistics.csv'

    def read(self, pk):
        with open(self._path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Id'] == pk:
                    return row

    def write(self, pk, username):
        #row = dict(self.read(pk))
        with open(self._path, 'a') as file:
            create = csv.DictWriter(file, fieldnames=fieldList)
            create.writeheader()
            create.writerow({
                'Id': pk,
                'Username': username,
                'Notes_count': 0,
                'Monday': 0,
                'Tuesday': 0,
                'Wednesday': 0,
                'Thursday': 0,
                'Friday': 0,
                'Saturday': 0,
                'Sunday': 0,
            })


# result = StatisticsFile()
# #result.write(1,'Rem')
#
# r = result.read('1')
# print(r)
