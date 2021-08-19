# importing modules
import password_generator
import crypt 
import json 

# asking 
user_input = input('Pour quelle plateforme ?\n') # à mettre dans mai.py
user_id = input('Votre login:\n') # à mdans le fichier main.py

# printing the password
password = crypt.encrypted
print(f'Password:\n{password_generator.the_pass}')

# organized data 
odata = { # Trouver un moyen pour rassembler tout les mdps dans un seul fichier
    user_input: {
    'Login':user_id,
    'Password': password
    }
}

# adding password in file
def add_pass(): # trouver un système pour ajouter ceci dans le fichier json
    with open('my_password.json', 'w') as fichier: 
        json.dump(odata, fichier, indent = 4)
add_pass()

