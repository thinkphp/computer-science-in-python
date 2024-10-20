def vigenere_cipher_preserve_case(text, key, mode='encrypt'):
    """
    Implementează cifrul Vigenère păstrând majusculele/minusculele și caracterele speciale.
    
    Args:
        text (str): Textul original
        key (str): Cheia de criptare
        mode (str): 'encrypt' pentru criptare sau 'decrypt' pentru decriptare
    
    Returns:
        str: Textul procesat
    """
    # Păstrăm textul original pentru a reține formatul
    result = ''
    key = key.upper()
    key_index = 0
    
    print(f"\nPROCES DE {mode.upper()}ARE:")
    print("=" * 50)
    print(f"Text original: {text}")
    print(f"Cheie: {key}")
    print("-" * 50)
    print("CALCULE:")
    
    for char in text:
        if char.isalpha():
            # Determinăm dacă caracterul este majusculă sau minusculă
            is_upper = char.isupper()
            
            # Convertim caracterul și cheia la majuscule pentru calcul
            char_num = ord(char.upper()) - ord('A')
            key_char = key[key_index % len(key)]
            key_num = ord(key_char) - ord('A')
            
            if mode == 'encrypt':
                # Pentru criptare: (text + cheie) mod 26
                new_num = (char_num + key_num) % 26
            else:
                # Pentru decriptare: (text - cheie + 26) mod 26
                new_num = (char_num - key_num + 26) % 26
            
            # Convertim înapoi în caracter, păstrând majuscula/minuscula originală
            new_char = chr(new_num + ord('A'))
            if not is_upper:
                new_char = new_char.lower()
            
            print(f"Poziția {key_index + 1}:")
            print(f"  Caracter original: {char}")
            print(f"  Caracter cheie: {key_char}")
            if mode == 'encrypt':
                print(f"  Calcul: ({char_num} + {key_num}) % 26 = {new_num}")
            else:
                print(f"  Calcul: ({char_num} - {key_num} + 26) % 26 = {new_num}")
            print(f"  Rezultat: {new_char}\n")
            
            key_index += 1
            result += new_char
        else:
            # Păstrăm caracterele non-alfabetice neschimbate
            result += char
    
    print("=" * 50)
    print("REZULTAT FINAL:")
    print(f"Text {'criptat' if mode == 'encrypt' else 'decriptat'}: {result}")
    return result

# Demonstrație cu textul "Adrian"
text_original = "Adrian"
cheie = "Adrian"

print("\nPROCES COMPLET DE CRIPTARE ȘI DECRIPTARE:")
print("=" * 50)

# Criptare
text_criptat = vigenere_cipher_preserve_case(text_original, cheie, 'encrypt')

print("\n" + "=" * 50)

# Decriptare
text_decriptat = vigenere_cipher_preserve_case(text_criptat, cheie, 'decrypt')
