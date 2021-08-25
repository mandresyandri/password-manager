# importing modules
import new_password

# User action
print('Bonjour, comment puis-je vous aider ?')
request_user = input('["Create"] Créer un nouveau mot de passe | ["Show"] Consulter les mot de passe ')
if request_user in ['Create', 'Create ', 'create', 'create ']:
    new_password.adding_pass()
elif request_user in ['Show', 'Show ', 'show', 'show ']:
    print('Afficher le mot de passe')
