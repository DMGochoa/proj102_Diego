"""


Diego Alejandro Moreno Gallón
17/01/2023
"""
import csv

class csv_control():
    """
    Specific Class to read a csv (DB) of passwords for each app
    """
    def __init__(self, pathfile) -> None:
        self.path = pathfile
        self.data = dict()
    
    def read_csv(self):
        """
        Method that read the csv file that was specify in self.path and update the self.data
        """
        data = dict()
        with open(self.path, 'r') as file:
            reader = csv.DictReader(file) # Iterable with all the rows
            for i in reader:
                data[i['app_name']] = i
        self.data
    
    def add_data(self, info=dict()):
        with open(self.path, 'w') as file:
            reader = csv.DictReader(file) # Iterable with all the rows
            for i in reader:
                data[i['app_name']] = i
        self.data
    
    

def save_pass(password, pathfile):
    pass

if __name__ == '__main__':
    csv_table = csv_control('./data.csv')
    print(csv_table.data)#csv_table.read_csv().keys())
