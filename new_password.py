# importing modules
from crypt import decrypt_cesar, encrypt_cesar
import password_generator
import crypt 
import json 
# the function
def adding_pass():
    # Asking for the platform and the login
    platform = input('Pour quelle plateforme ?\n')
    login = input('login:\n')
    # Showing the pass 
    mdp = password_generator.the_pass
    print(f'Votre mot de passe est: \n{mdp}')
    # Crypting the password
    e_mdp = crypt.encrypt_cesar(mdp)
    the_password = {
        "Plateforme": platform,
        "Login:": login, 
        "Mot de passe": e_mdp
    }
    with open('my_password.json', 'w') as fichier:
        json.dump(the_password, fichier, indent = 4 )
