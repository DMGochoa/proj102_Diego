"""

"""
from app import app

def menu_1():
    quit_menu_1 = False
    app_opt = app()
    while not quit_menu_1:
        app_opt.clean_screen()
        decision1 = app_opt.presentation() # presentation
        if decision1 == 1: # Login
            menu_2(app_opt) # Menu to Login
        elif decision1 == 2: # New User
            menu_3(app_opt) # Menu to create New use
        elif decision1 == 3: # Quit
            quit_menu_1 = True


# Notas:
# Menu 2 y 3 son como menus de paso y se podrian combinar como una clase a parte

def menu_2(app_opt):
    quit_menu_2 = False
    while not quit_menu_2:
        app_opt.clean_screen()
        user_data = app_opt.request_info() # Request for the user data
        app_opt.clean_screen()
        # Shows if the login was successfull
        result = app_opt.login(user_data[0], user_data[1]) # Validation data
        if result:
            # Success in validation
            # Menu 4
            print('1')
            quit_menu_2 = True
        else:
            # No succes in validation
            if app_opt.repeat():
                quit_menu_2 = True
                
def menu_3(app_opt): 
    quit_menu_3 = False
    while not quit_menu_3:
        app_opt.clean_screen()
        user_data = app_opt.request_info() # Request for the user data
        app_opt.clean_screen()
        result = app_opt.new_user(user_data[0], user_data[1])
        if result:
            # Successfully created
            # Menu 4
            quit_menu_3 = True
        else:
            # No succes in cretion
            if app_opt.repeat():
                quit_menu_3 = True
        
    
def main():
    menu_1()


if __name__ == '__main__':
    main()