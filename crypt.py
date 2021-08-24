import password_generator
# Function to encrypt 

def encrypt_cesar(password): 
    changement_ASCII = [ord(element) for element in password] #ord: STR => ASCII != chr
    algo_cesar = [numbers + 3 for numbers in changement_ASCII]
    to_encrypte = [chr(numbers) for numbers in algo_cesar]
    encrypte = ''.join(element for element in to_encrypte)
    return encrypte
# debug: a = encrypt_cesar("abc")
# debug: print(encrypt_cesar("abc"))
def decrypt_cesar(password):
    changement_ASCII = [ord(element) for element in password]
    contre_algo = [numbers - 3 for numbers in changement_ASCII]
    changement_str = [chr(element) for element in contre_algo]
    decrypt = ''.join(element for element in changement_str)
    return decrypt
# debug: print(decrypt(a))
