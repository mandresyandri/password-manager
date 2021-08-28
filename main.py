# importing modules
import authentification
import json
# Authentification
first_request_user = input('Avez-vous un compte ?[y|n]')
if first_request_user == 'y': # continuer à coder
   authentification.account_login()
   if name == user_data['login']:
        password = input('password: ')
        if password == user_data['Mot de passe']:
            print(f'Bonjour {name}, comment puis-je vous aider ?')
            request_user = input('["Create"] Créer un nouveau mot de passe | ["Show"] Consulter les mot de passe ')
            if request_user in ['Create', 'Create ', 'create', 'create ']:
                new_password.adding_pass()
            elif request_user in ['Show', 'Show ', 'show', 'show ']:
                show_password.show()

elif first_request_user == 'n':
   authentification.create_account_login()
   print('votre compte a bien été créé')
