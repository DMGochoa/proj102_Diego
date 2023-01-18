motorcycles = ['honda', 'yamaha',
              'suzuki', 'BMW']
print(sorted(motorcycles))
motorcycles.sort()
print(motorcycles)

# iter

for motorcycle in motorcycles:
    print(motorcycle)
    
for i in range(len(motorcycles)):
    print(i)
    
# list

listas = [i for i in range (5)]
print(listas)

# tuple

tpl = ('elem1', 'elem2', 'elem3')

print(tpl[0], tpl[-1])

# Accesing str, list, tuple

names = ['Jose', 'Miguel', 'Carlos']
my_str = 'Hellow World'

print(names[1:], tpl[1:], my_str[3:6])

print([item for item in my_str if item != ' '])

# File Reader

# One way
file = open('txt_for_class3.txt')
# process
file.close()

# Second way
with open('txt_for_class3.txt') as file:
    print(file.read())
    for line in file:
        print(line)
