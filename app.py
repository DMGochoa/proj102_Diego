
import os # Paths manage
import shutil # Copy and paste files
from crypto import Crypto 

class app:
    
    def __init__(self) -> None:
        pass
      
    def login(self, user:str, password:str) -> bool:
        """This method is to make the validation of the user when logging in

        Args:
            user (str): _description_
            password (str): _description_

        Returns:
            bool: If the user is valid or not.
        """
        # The next two lines get the User directory
        current_dir = os.getcwd()
        user_dir = os.path.join(current_dir, 'Users', user)
            
        # Verify if the user directory exist
        if os.path.exists(user_dir):
            # Path to the crypt password and read the file to take the crypt password
            pcrypt = os.path.join(user_dir, 'pcrypt.txt')
            with open(pcrypt, 'r') as file:
                pass_crypt = file.readline()
            # Verify if the key is the password
            if password == Crypto(password).decrypt(pass_crypt):
                print('Satisfactory login')
                return True
            else:
                print('Wrong Password')
                return False
        else:
            print('Unsatisfactory login')
            return False
    
    def new_user(self, user:str, password:str) -> bool:
        # The next three lines get the user directory
        current_dir = os.getcwd()
        user_dir = os.path.join(current_dir, 'Users', user)
        # The template path and the path for files in the directory
        temp_dir = os.path.join(current_dir, 'Users', 'template')
        temp_files = os.listdir(temp_dir)
        # Verify if the user directory exist
        if os.path.exists(user_dir):
            print(f'The username {user} is already created')
            return False
        else:
            os.mkdir(user_dir) # Make the user directory
            # Copy the template files in the new user directory
            for temp_file in temp_files:
                origin = os.path.join(temp_dir, temp_file)
                target = os.path.join(user_dir, temp_file)
                shutil.copyfile(origin, target)
            # Encrypt the password with password and save the key in the pcrypt
            with open(os.path.join(user_dir, 'pcrypt.txt'), 'w') as file:
                file.write(Crypto(password).encrypt(password))
            print('The user was successfully created')
            return True
    
    def presentation(self) -> int:
        # Present the app
        print("This app is for saving applications and their corresponding password. Please\ntype the number of the action you want to perform and press enter.")
        # First three options of the app
        print("Options:")
        print("\t1. Login")
        print("\t2. New User")
        print("\t3. Quit")
        return int(input('Option number: '))
    
    def clean_screen(self) -> None:
        # Clear the screen
        os.system('clear')
    
    def request_info(self) -> tuple:
        # Request info
        print('Enter the following data:')
        user_name = input('Username: ')
        user_pass = input('Password: ')
        return user_name, user_pass
    
    def repeat(self) -> bool:
        print('Please type the number of the action you want to perform and press enter.')
        print('Options:')
        print("\t1. Try again")
        print("\t2. Return")
        return int(input('Option number: ')) == 2
    
            
if __name__ == '__main__':
    prueba = app()
    print(prueba.login(user='template', password='1234'))
    print(prueba.new_user('Juan', '1234'))
    print(prueba.ingresar(user='Juan', password='1234'))
    os.rmdir(os.path.join(os.getcwd(), 'Users', 'Juan'))            