import csv




class StatisticsFile:

    def __init__(self,username):
        self._path = 'statistics.csv'
        self._username = username

    def readByUsername(self):
        with open(self._path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if self._username in row['Username']:
                    print(True)

    def writeNewUser(self):
        pass



file_statistics = StatisticsFile('REM')
file_statistics.readByUsername()
