Termenul **„cromozom fezabil”** apare în principal în contextul **algoritmilor genetici**, care sunt metode inspirate de evoluția naturală folosite pentru rezolvarea unor probleme de optimizare sau căutare.

---

### 🔬 Ce este un **cromozom** în algoritmi genetici?

În acest context, un **cromozom** este o **reprezentare a unei soluții candidate** la problema pe care încerci să o rezolvi. Poate fi sub formă de:

* un șir binar (ex: `101101`),
* un vector de numere,
* o permutare (ex: ordinea orașelor într-o problemă de tipul „turul orașelor”).

---

### ✅ Ce înseamnă **fezabil**?

O soluție este **fezabilă** dacă respectă toate **restricțiile** impuse de problemă. Așadar, un **cromozom fezabil** este:

> **un cromozom (soluție) care respectă toate constrângerile problemei și poate fi considerat valid.**

---

### 📌 Exemplu:

Să presupunem că vrei să rezolvi o problemă de împachetare a obiectelor într-un rucsac (`knapsack problem`):

* Capacitatea rucsacului: 10 kg.
* Ai 5 obiecte, fiecare cu o greutate și o valoare.

Dacă un cromozom selectează obiectele 2, 4 și 5, iar greutatea totală este 8 kg, atunci:

* **cromozomul este fezabil**.

Dacă însă greutatea totală este 14 kg:

* **cromozomul este nefezabil** – încalcă restricția de capacitate.

---

### 🧠 Concluzie

**Cromozom fezabil** = soluție validă în algoritmi genetici, care respectă toate regulile și restricțiile problemei.


În algoritmii genetici, un **cromozom fezabil** (sau **soluție fezabilă**) se referă la un cromozom (soluție candidată) care **respectă toate constrângerile problemei** și se află în **spațiul soluțiilor valide**. Acesta este un concept fundamental deoarece doar cromozomii fezabili pot reprezenta soluții reale, aplicabile în practică.  

### Caracteristici cheie:
1. **Respectă constrângerile**  
   - Fiecare problemă are constrângeri specifice (ex: limite de resurse, reguli de validitate, condiții fizice).  
   - *Exemplu*: În problema rucsacului, un cromozom fezabil nu poate depăși capacitatea maximă a rucsacului.  

2. **Reprezintă o soluție validă**  
   - Cromozomul trebuie să aibă o structură corectă (ex: în problemele de tip permutare, fiecare element trebuie să apară exact o dată).  

3. **Poate fi evaluat prin funcția de fitness**  
   - Doar cromozomii fezabili primesc o evaluare de fitness completă. Soluțiile infezabile sunt fie eliminate, fie penalizate.  

### Exemple practice:
- **Problema comis-voiajor (TSP)**:  
  Un cromozom fezabil este o **permutare validă** a orașelor (fiecare oraș vizitat o singură dată, fără repetiții sau omisiuni).  
  - *Infezabil*: `[A, B, A, D]` (orașul `A` apare de două ori).  
  - *Fezabil*: `[A, B, C, D]`.  

- **Problema rucsacului**:  
  Un cromozom fezabil selectează obiecte fără a depăși capacitatea rucsacului.  
  - *Infezabil*: Greutate totală = 15 kg (dacă capacitatea maximă este 10 kg).  

- **Problema planificării resurselor**:  
  Un cromozom fezabil nu depășește disponibilitatea resurselor (ex: ore de lucru, materii prime).  

### De ce este important?
- **Eficiență algoritmică**: Evaluarea soluțiilor infezabile poate fi irositoare de resurse.  
- **Calitatea soluției finale**: Algoritmii genetici converg mai rapid spre soluții optime când operează pe spații fezabile.  
- **Aplicabilitate practică**: Soluțiile infezabile sunt inutile în scenarii reale.  

### Tecnici de gestionare a infezabilității:
1. **Funcții de penalizare**:  
   - Cromozomii infezabili primesc un fitness scăzut (ex: fitness negativ) pentru a reduce șansa de selecție.  
2. **Operatorii genetici specializați**:  
   - Se folosesc operatori de crossover (ex: **PMX**, **OX**, **CX**) și mutații care **păstrează fezabilitatea** (ex: pentru permutări).  
3. **Repararea soluțiilor**:  
   - Transformă cromozomii infezabili în fezabili prin ajustări locale (ex: eliminarea duplicatelor într-o permutare).  
4. **Reprezentări restrictive**:  
   - Alegerea unei reprezentări a cromozomilor care garantează fezabilitatea (ex: codificare binară cu constrângeri încorporate).  

### Concluzie:
Un **cromozom fezabil** este coloana vertebrală a algoritmilor genetici aplicați în probleme complexe cu constrângeri. Asigurarea fezabilității (prin designul operatorilor și reprezentării) este esențială pentru obținerea de soluții relevante și de înaltă calitate.
