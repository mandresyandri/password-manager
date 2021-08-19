# importing modules
import new_password

# User action
request_user = input('Bonjour, comment puis-je vous aider ?\n["Create"] Créer un nouveau mot de passe | ["Show"] Consulter les mot de passe')
if request_user == 'Create': 
    new_password.add_pass()
else: 
    pass # Think about code structure 

