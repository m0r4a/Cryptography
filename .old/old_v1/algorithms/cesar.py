#!/bin/python3

def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            # Revisar si es mayus o minus 
            is_uppercase = char.isupper()
            
            # Calculamos el nuevo index
            index = (ord(char) - ord('A' if is_uppercase else 'a') + shift) % 26
            
            # Consiguiendo la letra encriptada
            encrypted_char = chr(index + ord('A' if is_uppercase else 'a'))
            
            result += encrypted_char
        else:
            result += char
    return result

def show_transpositions(message):
    for shift in range(26):
        result = caesar_cipher(message, shift)
        print(f"+{shift}: {result}")

def generate_decryption_dictionary(shift):
    decryption_dictionary = {}
    for i in range(26):
        index = (i - shift) % 26
        encrypted_char = chr(i + ord('A'))
        decrypted_char = chr(index + ord('a'))
        decryption_dictionary[encrypted_char] = decrypted_char
    
    return decryption_dictionary

# Pedir el mensaje encriptado
encrypted_message = input("Enter the encrypted message: ")

# Mostrar todas los saltos/trasposicón/lo que sea
show_transpositions(encrypted_message)

# Pedir la trasposición o eso, correcta
while True:
    try:
        correct_transposition = int(input("\nEnter the correct transposition: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Mostrar el diccionario o eso, sale en el libro y queda más bonito
result = caesar_cipher(encrypted_message, correct_transposition)
print(f"\nDecrypted message with transposition {correct_transposition}: {result}")

decryption_dictionary = generate_decryption_dictionary(correct_transposition)
print("\nDecryption dictionary:")
for encrypted_char, decrypted_char in decryption_dictionary.items():
    print(f"{encrypted_char} -> {decrypted_char}")

    # Printeas el mensaje desencriptado
decrypted_message = caesar_cipher(encrypted_message, correct_transposition)
print(f"\nDecrypted message: {decrypted_message}")
