# coding: utf-8
# importing modules
import json
import crypt


def show():
    with open('my_password.json', 'r') as file:
        the_password = json.load(file)
    decrypted = crypt.decrypt_cesar(the_password['Mot de passe'])
    the_password['Mot de passe'] = decrypted
    print(the_password)
