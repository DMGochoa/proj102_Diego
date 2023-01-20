def print_pet_information(pet_type):
    print(f'I have my pet that is a {pet_type}')

print_pet_information('dog')
print_pet_information('cat')

def make_full_name(first_name: str, last_name: str) -> str: # Informa que tipos de datos se debe entrar y retornar
    return first_name + ' ' + last_name

def make_full_name(first_name, last_name, middle_name=''):
    if middle_name:
        return first_name + ' ' + middle_name + ' ' + last_name
    else:
        return first_name + ' ' + last_name


print('The full name is:', make_full_name('Diego', 'Moreno'))

print('The full name is:', make_full_name('Diego', 'Moreno', 'Alejandro'))

def make_pizza(*args, **kargs):
    print(args) # retorna tupa
    print(kargs) # retorna dict

make_pizza(uno=1, dos=2, tres=3)
make_pizza(hola={'uno':1, 'dos':2, 'tres':3})
make_pizza(1,2,3,4,5, hola=1)