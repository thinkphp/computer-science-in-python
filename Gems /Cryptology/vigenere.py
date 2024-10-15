class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()

    def _extend_keyword(self, length):
        """ Repeats the keyword to match the length of the plaintext or ciphertext """
        repeats = (length // len(self.keyword)) + 1
        return (self.keyword * repeats)[:length]

    def encrypt(self, plaintext):
        ciphertext = []
        keyword_extended = self._extend_keyword(len(plaintext))
        
        for p_char, k_char in zip(plaintext, keyword_extended):
            if p_char.isalpha():
                base = ord('A') if p_char.isupper() else ord('a')
                shift = ord(k_char) - ord('A')
                encrypted_char = chr((ord(p_char.upper()) - ord('A') + shift) % 26 + base)
                ciphertext.append(encrypted_char)
            else:
                ciphertext.append(p_char)

        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        plaintext = []
        keyword_extended = self._extend_keyword(len(ciphertext))
        
        for c_char, k_char in zip(ciphertext, keyword_extended):
            if c_char.isalpha():
                base = ord('A') if c_char.isupper() else ord('a')
                shift = ord(k_char) - ord('A')
                decrypted_char = chr((ord(c_char.upper()) - ord('A') - shift + 26) % 26 + base)
                plaintext.append(decrypted_char)
            else:
                plaintext.append(c_char)

        return ''.join(plaintext)


# Exemplu de utilizare
if __name__ == "__main__":
    keyword = input("Introduceți cuvântul cheie: ")
    plaintext = input("Introduceți textul clar: ")

    cipher = VigenereCipher(keyword)
    
    encrypted = cipher.encrypt(plaintext)
    print(f"Text criptat: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Text decriptat: {decrypted}")
