import json
import crypt 
import os
# condition 
def login():
    user_login = input('Login: \n')
    user_pass = input('Mot de passe: \n')
    the_login = {
        "login": user_login,
        "Mot de passe": user_pass
    }
    the_login["Mot de passe"] = crypt.encrypt_cesar(user_pass)
    with open("initial_login.json", 'w') as file:
        json.dump(the_login, file, indent=4)
login()
