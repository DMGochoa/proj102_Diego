"""
python3 review_file.py -i build0
 
Have index = 2
 
.1.3.6.1.2.1.2.2.1.2 = STRING: build0
.1.3.6.1.2.1.2.2.1.3 = INTEGER: ethernetCsmacd(6)
.1.3.6.1.2.1.2.2.1.4 = INTEGER: 1500
.1.3.
"""
import optparse
opts = optparse.OptionParser()

opts.add_option("-f", "--file", dest='fname', help="This is the file name that you would like to read")
opts.add_option("-i", "--index", dest='iname', help="This is the i name")

(options, arguments) = opts.parse_args()

file = open(options.fname, 'r')

table = dict()
# Code for the fname
code_num = ''


for line in file:
    elements = line.split()
    
    if elements[-1] == options.iname:
        code_num = elements[0][0:18] # Code numbers
        second_num = elements[0][18:20]
        type_var = elements[-2] # Select the type
        #size = len(elements[0])
        identificator_final = elements[0][20:22]
        print('-'*10, 'INICIO', '-'*10)
        print(code_num + second_num, identificator_final, type_var, elements[-1])
        
    elif code_num == elements[0][0:18]:
        if identificator_final == elements[0][20:22]:
            second_num = elements[0][18:20]
            type_var = elements[-2] # Select the type
            print(code_num + second_num, identificator_final, type_var, elements[-1])
        
    