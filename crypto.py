"""
Module for encrypting and decrypting text by providing a password
"""
import cryptocode

class Crypto:
    def __init__(self, password:str) -> None:
        self.password = password
        
    def encrypt(self, text:str) -> str:
        return cryptocode.encrypt(text, self.password)
    
    def decrypt(self, crypt_text:str) -> str:
        return cryptocode.decrypt(crypt_text, self.password)
    
if __name__ == '__main__':
    prueba = Crypto('1234')
    enc = prueba.encrypt('1234')
    enc2 = prueba.encrypt('1234')
    print(enc)
    print(enc2)
    print(prueba.decrypt(enc))
    print(prueba.decrypt(enc2))
    
    with open('./Users/template/pcrypt.txt', 'r') as file:
        print(prueba.decrypt(file.readline()))
   