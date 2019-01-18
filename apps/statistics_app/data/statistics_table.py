import csv




class StatisticsFile:

    def __init__(self):
        self._path = 'statistics.csv'

    def readByUsername(self, pk):
        with open(self._path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Id'] == pk:
                    return row

    def writeNewUser(self):
        pass



file_statistics = StatisticsFile()
result =  file_statistics.readByUsername('1')
print(result)
