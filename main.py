# importing modules
import authentification
import json
# Authentification
first_request_user = input('Avez-vous un compte ?[y|n]')
if first_request_user == 'y':
   authentification.account_login()

elif first_request_user == 'n':
    authentification.create_account_login()
