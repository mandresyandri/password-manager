import json
import crypt 
import show_password
import new_password
import os
# condition 
def create_account_login():
    # Verifing 
    if os.path.isfile('initial_login.json') == True: 
         pass
    else: # Create new_user
        user_login = input('Login: \n')
        user_pass = input('Mot de passe: \n')
        the_login = {
            "login": user_login,
            "Mot de passe": user_pass
        }
        the_login["Mot de passe"] = crypt.encrypt_cesar(user_pass)
        with open("initial_login.json", 'w') as file:
            json.dump(the_login, file, indent=4)

def account_login():
    name = input('login: ')
    with open('initial_login.json', 'r') as file:
        user_data = json.load(file)
    if name == user_data['login']:
        password = input('password: ')
        if password == user_data['Mot de passe']:
            print(f'Bonjour {name}, comment puis-je vous aider ?')
            request_user = input('["Create"] Créer un nouveau mot de passe | ["Show"] Consulter les mot de passe ')
            if request_user in ['Create', 'Create ', 'create', 'create ']:
                new_password.adding_pass()
            elif request_user in ['Show', 'Show ', 'show', 'show ']:
                show_password.show()