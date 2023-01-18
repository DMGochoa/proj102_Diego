"""
Function to read a csv file and convert into a dict
"""
from Exercise1 import payment

def read_csv(pathfile='./employees.csv', no_elements=3):
    elements = list()
    with open(pathfile, 'r') as file:
        head = file.readline()
        lines = file.readlines()
        
    for line in lines:
        if len(line) < no_elements:
            continue
        
        elements.append(line.replace('\n', '').split(','))
    
    return elements

if __name__ == '__main__':
    employees = read_csv()
    
    for employee in employees:
        print(employee[0], ' will be paid: ', payment(int(employee[1]), float(employee[2])))
