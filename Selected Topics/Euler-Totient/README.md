# Euler's Totient


### Totientul unui Număr (\( \phi(n) \))  
Funcția Euler, notată cu \( \phi(n) \), reprezintă numărul de întregi pozitive mai mici sau egale cu \( n \) care sunt **prime cu \( n \)**, adică împart cu \( n \) doar factorul \( 1 \).

---

## **Proprietăți Importante**

1. **Numere Prime**  
   Dacă \( n \) este un număr prim, atunci:
   \[
   \phi(n) = n - 1
   \]
   deoarece toate numerele mai mici decât \( n \) sunt prime cu acesta.

2. **Funcția Totient este Multiplicativă**  
   Dacă \( m \) și \( n \) sunt numere prime între ele (\( \text{gcd}(m, n) = 1 \)), atunci:
   \[
   \phi(m \cdot n) = \phi(m) \cdot \phi(n)
   \]

3. **Formula Generală**  
   Funcția totient pentru un număr \( n \) se poate calcula folosind factorii săi primi:
   \[
   \phi(n) = n \cdot \prod_{p | n} \left(1 - \frac{1}{p}\right)
   \]
   Unde \( p \) reprezintă toți divizorii primi ai lui \( n \).

---

## **Exemplu Practic**  

Pentru \( n = 12 \):  
- Divizorii primi ai lui \( 12 \) sunt \( 2 \) și \( 3 \).  
- Aplicând formula:
  \[
  \phi(12) = 12 \cdot \left(1 - \frac{1}{2}\right) \cdot \left(1 - \frac{1}{3}\right)
  \]
  \[
  \phi(12) = 12 \cdot \frac{1}{2} \cdot \frac{2}{3} = 4
  \]
- Numerele mai mici sau egale cu 12 care sunt prime cu 12 sunt: \( 1, 5, 7, 11 \).

---
Here is the content formatted for a GitHub README.md file:

```markdown
# Totient Function (\( \phi(n) \))

The Euler's totient function, denoted as \( \phi(n) \), represents the number of positive integers less than or equal to \( n \) that are **coprime with \( n \)** (i.e., their greatest common divisor with \( n \) is 1).

---

## Properties

1. **For Prime Numbers**  
   If \( n \) is a prime number:
   \[
   \phi(n) = n - 1
   \]
   All numbers less than \( n \) are coprime with \( n \).

2. **Multiplicative Property**  
   The totient function is **multiplicative**, meaning:
   \[
   \phi(m \cdot n) = \phi(m) \cdot \phi(n)
   \]
   if \( \text{gcd}(m, n) = 1 \).

3. **General Formula**  
   For any integer \( n \), the totient function can be calculated as:
   \[
   \phi(n) = n \cdot \prod_{p | n} \left(1 - \frac{1}{p}\right)
   \]
   Where \( p \) are the prime factors of \( n \).

---

## Example Calculation

For \( n = 12 \):  
- Prime factors of \( 12 \) are \( 2 \) and \( 3 \).  
- Using the formula:
  \[
  \phi(12) = 12 \cdot \left(1 - \frac{1}{2}\right) \cdot \left(1 - \frac{1}{3}\right)
  \]
  \[
  \phi(12) = 12 \cdot \frac{1}{2} \cdot \frac{2}{3} = 4
  \]
- Numbers less than or equal to 12 that are coprime with 12 are: \( 1, 5, 7, 11 \).

---

## Applications

1. **Cryptography**  
   - Used in encryption algorithms like **RSA**, where modular arithmetic is essential.

2. **Number Theory**  
   - Helps calculate the order of elements in cyclic groups.
   - Solves problems involving modular inverses and residues.

3. **Diophantine Equations**  
   - Appears in solving equations of the form \( ax \equiv b \ (\text{mod} \ n) \).

---

## Example Table

| \( n \) | Prime Factors of \( n \) | \( \phi(n) \)                              | Numbers Coprime with \( n \)             |
|--------|---------------------------|--------------------------------------------|------------------------------------------|
| 6      | \( 2, 3 \)                | \( 6 \cdot (1 - \frac{1}{2}) \cdot (1 - \frac{1}{3}) = 2 \) | \( 1, 5 \)                               |
| 15     | \( 3, 5 \)                | \( 15 \cdot (1 - \frac{1}{3}) \cdot (1 - \frac{1}{5}) = 8 \) | \( 1, 2, 4, 7, 8, 11, 13, 14 \)          |
| 17     | \( 17 \) (prime)          | \( 17 - 1 = 16 \)                          | \( 1, 2, 3, \dots, 16 \)                 |

---

This document provides an overview of the totient function and its practical applications in number theory and cryptography.
```
