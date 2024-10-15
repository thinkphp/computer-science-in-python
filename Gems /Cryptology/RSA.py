import math

# Funcție pentru a găsi gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Funcție pentru a calcula puterea modulară
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Funcție pentru inversul modular folosind algoritmul extins Euclid
def mod_inverse(e, phi):
    t, new_t = 0, 1
    r, new_r = phi, e

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        return None
    if t < 0:
        t = t + phi
    return t

# Inițializăm valorile pentru RSA
p = 61  # Prim 1
q = 53  # Prim 2
n = p * q  # n = p * q
phi = (p - 1) * (q - 1)  # Calculăm phi(n)

# Alegem cheie publică e
e = 17
while gcd(e, phi) != 1:
    e += 1

# Calculăm cheia privată d
d = mod_inverse(e, phi)

# Criptare
message = 65  # Mesaj de criptat
encrypted = mod_exp(message, e, n)
print(f"Mesaj criptat: {encrypted}")

# Decriptare
decrypted = mod_exp(encrypted, d, n)
print(f"Mesaj decriptat: {decrypted}")
