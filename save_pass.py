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
        self.read_csv()
    
    def read_csv(self) -> None:
        """
        Method that read the csv file that was specify in self.path and update the self.data
        """
        data = dict()
        with open(self.path, 'r') as file:
            reader = csv.DictReader(file) # Iterable with all the rows
            # We iterate all the rows and save them in a dict with index of the app_name
            for i in reader:
                data[i['app_name']] = i
            self.header = list(i.keys())
        self.data = data 
    
    def add_data(self, info:dict) -> None:
        """Adding the new row to the data table

        Args:
            info (dict, optional): A dictionary with 3 the keys (columns) and the respective 
            values. Defaults to dict().
        """
        self.data[info['app_name']] = info
        
    def save_csv(self) -> None:
        with open(self.path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.header)
            writer.writeheader() # write the header 
            # Save the info in each row
            for row in self.data.values():
                writer.writerow(row)
                
    def key_list(self):
        return list(self.data.keys())


if __name__ == '__main__':
    csv_table = csv_control('./data.csv')
    print(csv_table.header)
    for key, value in csv_table.data.items():
        print(key, value)
        
    new = {'app_name':'Youtube', 'creation_date':'20/01/2023', 'password':4}
    csv_table.add_data(new)
    print('\n'*2, 'New row was add')
    for key, value in csv_table.data.items():
        print(key, value)
    
    print(csv_table.key_list())
    csv_table.save_csv()
    
    
