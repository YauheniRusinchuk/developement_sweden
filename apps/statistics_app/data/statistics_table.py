import csv



class StatisticsFile:

    def __init__(self):
        self._path = 'statistics.csv'

    def read(self, pk):
        with open(self._path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Id'] == pk:
                    return row

    def write(self, pk):
        row = dict(self.read(pk))
        print(row)


file_statistics = StatisticsFile()
file_statistics.write('1')
