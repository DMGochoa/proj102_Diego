
import os
from crypto import Crypto

def ingresar(user:str, password:str) -> bool:
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
                return True
            else:
                return False
        else:
            return False
            
if __name__ == '__main__':
    print(ingresar(user='template', password='1234'))