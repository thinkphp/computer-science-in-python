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

## **Aplicații ale Funcției Totient**

1. **Criptografie**  
   - Funcția totient este utilizată în algoritmi de criptare, cum ar fi **RSA**, datorită legăturii sale cu proprietățile aritmetice modulare.

2. **Teoria Numerelor**  
   - Este esențială pentru a calcula ordinul elementelor în grupuri ciclice și pentru a rezolva probleme legate de resturi modulare.

3. **Ecuații Diofantice**  
   - Funcția totient apare frecvent în rezolvarea ecuațiilor de tip \( ax \equiv b \ (\text{mod} \ n) \).

---

## **Tabel Exemplu**  

| \( n \) | Divizori Primi ai lui \( n \) | \( \phi(n) \) | Numere Prime cu \( n \) |
|--------|-------------------------------|---------------|--------------------------|
| 6      | \( 2, 3 \)                   | \( 6 \cdot (1 - \frac{1}{2}) \cdot (1 - \frac{1}{3}) = 2 \) | \( 1, 5 \)              |
| 15     | \( 3, 5 \)                   | \( 15 \cdot (1 - \frac{1}{3}) \cdot (1 - \frac{1}{5}) = 8 \) | \( 1, 2, 4, 7, 8, 11, 13, 14 \) |
| 17     | \( 17 \) (prim)              | \( 17 - 1 = 16 \) | \( 1, 2, 3, \dots, 16 \) |

---

Acest document oferă o bază solidă pentru înțelegerea funcției Euler și aplicațiile sale practice.
