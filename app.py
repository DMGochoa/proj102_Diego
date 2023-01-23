
import os # Paths manage
import shutil # Copy and paste files
import datetime
from crypto import Crypto 
from save_pass import csv_control
from pass_gen import password_gen

class app:
    
    def __init__(self) -> None:
        pass
    
    def __user_session(self, user_dir):
        user_table_file = os.path.join(user_dir, 'data.csv')
        self.__table_controler = csv_control(user_table_file)
        
    def show_apps(self):
        print('The created passwords are')
        counter = 0
        for app in self.__table_controler.key_list():
            counter += 1
            print(f'\t{counter}. {app}')
            
    def new_app(self):
        print('Enter the following data:')
        app_name = input('App name: ')
        creation_date = datetime.date.today().strftime("%d/%m/%y")
        while True:
            self.clean_screen()
            print('Please type the number of the action you want to perform and press enter.')
            print('Options:')
            print("\t1. You will enter only the size")
            print("\t2. You will specify amounts of uppercase, lowercase, \n\tnumbers and special characters.")
            if int(input('Option number: ')) == 1:
                length = int(input('Enter the size (minimum 8): '))
                if length >= 8:
                    password = password_gen(length=length)
                    break
            elif int(input('Option number: ')) == 2:
                print('The sum of sizes needs to be equal or greatter than 8')
                upper = input('Enter the amount of uppercase letters: ')
                lower = input('Enter the amount of lowercase letters: ')
                num = input('Enter the amount of numbers: ')
                es_char = input('Enter the amount of especial characters: ')
                def_tuple = (upper, lower, num, es_char)
                if sum(def_tuple) >= 8:
                    password = password_gen(expects=def_tuple)
                    break
        self.clean_screen()
        print(f'For the app {app_name} the new password is {password}')
        password = Crypto(self.__password).encrypt(password)
        new_row = {'app_name':app_name, 'creation_date':creation_date, 'password':password}
        self.__table_controler.add_data(new_row)
        
    def save(self):       
      self.__table_controler.save_csv()
      
    def es_app(self):
        while True:
            self.clean_screen()
            app_name = input('Please enter the app name: ')
            app_info = list(self.__table_controler.specific_app(app_name).values())
            if app_name:
                password = Crypto(self.__password).decrypt(app_info[2])
                print(f'For {app_info[0]} the password is {password} and was generated on {app_info[1]}')
                break
      
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
                self.__password = password
                self.__user_session(user_dir)
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
            self.__password = password
            self.__user_session(user_dir)
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
    
    def main_options(self) -> int:
        print('Please type the number of the action you want to perform and press enter.')
        print('Options:')
        print("\t1. Show apps names")
        print("\t2. New app")
        print("\t3. Show app password")
        print("\t4. Exit")
        return int(input('Option number: '))
    
            
if __name__ == '__main__':
    prueba = app()
    print(prueba.login(user='template', password='1234'))
    print(prueba.new_user('Juan', '1234'))
    print(prueba.ingresar(user='Juan', password='1234'))
    os.rmdir(os.path.join(os.getcwd(), 'Users', 'Juan'))            