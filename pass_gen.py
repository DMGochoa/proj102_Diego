"""
In this module we are going to create the necessary functions to create a password generator.

Diego Alejandro Moreno Gallón
17/01/2023
"""
import random

def password_gen(length=8, expects=tuple()):
    """_summary_

    Args:
        length (int, optional): Total length of the password. Defaults to 8.
        expects (tuple, optional): Tuple that must contain 4 integer items 
                                   specifying the number of uppercase letters, 
                                   lowercase letters, numbers and special characters.. Defaults to None.

    Returns:
        _type_: _description_
    """
    if len(expects) < 4:
        print('Number of elements need to be 4')
    
    # Diferent characters that we will use
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 
                 'v', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7',
               '8', '9', '0']
    chars = ['*', '+', '-', '/', '@', '_', '?',
             '!', '[', '{', '(', ')', '}', ']',
             ',', ';', '.', '>', '<', '~', '°',
             '^', '&', '$', '#', '"']
    
    # Condition if is a general password or if we need specific quantities
    if expects:
        # Lists to select a specific number of characters
        select_upper = [random.choice(uppercase) for _ in range(int(expects[0]))]
        select_lower = [random.choice(lowercase) for _ in range(int(expects[1]))]
        select_num = [random.choice(numbers) for _ in range(int(expects[2]))]
        select_char = [random.choice(chars) for _ in range(int(expects[3]))]
        # Create the password based on the characters list selections
        selected_elem = select_upper + select_lower + select_num + select_char
        password = ''.join(random.sample(selected_elem, len(selected_elem)))
    else:
        elements = uppercase + lowercase + numbers + chars
        # Create the password based in a list of random elements
        password = ''.join([random.choice(elements) for _ in range(length)])
    return password
        
if __name__ == '__main__':
    
    for i in range(10):
        print('#'*15, i, '#'*15)
        new_password = password_gen()
        print('The new password has a length of {}. \nThe new password is {}'.format(len(new_password), new_password))
    
    
    print('\n\nTest for specific requirements')
    lists_values = [[random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)] for _ in range(10)]
    gen_number = 1
    for values in lists_values:
        print('#'*15, gen_number, '#'*15)
        new_password = password_gen(expects=(values[0], values[1], values[2], values[3]))
        print('The new password has a length of {} and the input is {}. \nThe new password is {}'.format(len(new_password), sum(values), new_password))
        gen_number += 1

        