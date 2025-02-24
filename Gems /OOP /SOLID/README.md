Conceptul **SOLID** reprezintă un set de principii pentru programarea orientată pe obiecte (OOP), care ajută la crearea unui cod mai flexibil, ușor de întreținut și scalabil. Principiile au fost popularizate de **Robert C. Martin (Uncle Bob)** și sunt fundamentale în dezvoltarea de software robust.  

Iată o prezentare teoretică a fiecărui principiu:

---

### **S - Single Responsibility Principle (SRP)**  
🔹 **Principiul responsabilității unice** afirmă că **o clasă ar trebui să aibă un singur motiv să se schimbe**, adică o singură responsabilitate.  
✅ **Beneficii**: Codul devine mai ușor de înțeles, testat și modificat.  
📌 **Exemplu**:  
- O clasă `Raport` care se ocupă doar de generarea datelor raportului, iar o altă clasă `RaportPrinter` care se ocupă de afișarea raportului.  

---

### **O - Open/Closed Principle (OCP)**  
🔹 **Principiul deschis/închis** afirmă că **o entitate software (clasă, modul, funcție)** trebuie să fie **deschisă pentru extindere, dar închisă pentru modificare**.  
✅ **Beneficii**: Permite adăugarea de funcționalitate fără a modifica codul existent, reducând riscurile de introducere a erorilor.  
📌 **Exemplu**:  
- Folosirea interfețelor și a moștenirii pentru a adăuga noi comportamente fără a schimba codul de bază.  

---

### **L - Liskov Substitution Principle (LSP)**  
🔹 **Principiul substituției lui Liskov** susține că **obiectele unei clase derivate ar trebui să poată înlocui obiectele clasei de bază fără a altera corectitudinea programului**.  
✅ **Beneficii**: Asigură corectitudinea și predictibilitatea comportamentului atunci când se utilizează moștenirea.  
📌 **Exemplu**:  
- Dacă `Pătrat` moștenește `Dreptunghi`, atunci `Pătrat` trebuie să se comporte ca un `Dreptunghi` fără efecte neașteptate.  

---

### **I - Interface Segregation Principle (ISP)**  
🔹 **Principiul segregării interfeței** afirmă că **o clasă nu ar trebui să fie forțată să implementeze interfețe pe care nu le folosește**.  
✅ **Beneficii**: Se evită interfețele "grase" și se crează interfețe mai mici și mai specifice.  
📌 **Exemplu**:  
- În loc de o interfață mare `IMultifunctionalDevice`, putem avea `IPrint`, `IScan`, `IFax`.  

---

### **D - Dependency Inversion Principle (DIP)**  
🔹 **Principiul inversiunii dependențelor** afirmă că **modulele de nivel înalt nu ar trebui să depindă de modulele de nivel scăzut**, ci ambele ar trebui să depindă de abstracții.  
✅ **Beneficii**: Crește reutilizabilitatea și testabilitatea codului.  
📌 **Exemplu**:  
- În loc ca o clasă `Controller` să creeze direct o instanță `Service`, aceasta va primi `Service` ca dependență (prin constructor sau metode), favorizând injectarea dependențelor.  

---

Hai să luăm fiecare principiu **SOLID** și să-l ilustrăm cu un exemplu practic în **Python**.  

---

### **1. Single Responsibility Principle (SRP)**  
🔹 *O clasă trebuie să aibă o singură responsabilitate.*

#### ❌ **Exemplu greșit**:
```python
class Raport:
    def __init__(self, date):
        self.date = date

    def generare_raport(self):
        return f"Raport: {self.date}"

    def salvare_in_fisier(self, filename):
        with open(filename, 'w') as f:
            f.write(self.generare_raport())
```
*Problema:* Clasa `Raport` se ocupă atât de generarea raportului, cât și de salvarea lui, ceea ce încalcă SRP.

#### ✅ **Exemplu corect**:
```python
class Raport:
    def __init__(self, date):
        self.date = date

    def generare_raport(self):
        return f"Raport: {self.date}"

class RaportSalvare:
    @staticmethod
    def salvare_in_fisier(raport, filename):
        with open(filename, 'w') as f:
            f.write(raport.generare_raport())

# Utilizare
raport = Raport("Date importante")
RaportSalvare.salvare_in_fisier(raport, "raport.txt")
```
*✔ Acum fiecare clasă are o singură responsabilitate.*  

---

### **2. Open/Closed Principle (OCP)**  
🔹 *Clasa ar trebui să fie deschisă pentru extindere, dar închisă pentru modificare.*

#### ❌ **Exemplu greșit**:
```python
class CalculImpozit:
    def calculeaza(self, venit, tip):
        if tip == 'persoana_fizica':
            return venit * 0.1
        elif tip == 'firma':
            return venit * 0.2
```
*Problema:* Dacă vrem să adăugăm un alt tip, trebuie să modificăm metoda `calculeaza`.

#### ✅ **Exemplu corect**:
```python
from abc import ABC, abstractmethod

class StrategieImpozit(ABC):
    @abstractmethod
    def calculeaza(self, venit):
        pass

class ImpozitPersoanaFizica(StrategieImpozit):
    def calculeaza(self, venit):
        return venit * 0.1

class ImpozitFirma(StrategieImpozit):
    def calculeaza(self, venit):
        return venit * 0.2

# Utilizare
def calculeaza_impozit(strategie: StrategieImpozit, venit):
    return strategie.calculeaza(venit)

print(calculeaza_impozit(ImpozitPersoanaFizica(), 10000))  # 1000
print(calculeaza_impozit(ImpozitFirma(), 10000))          # 2000
```
*✔ Putem adăuga alte clase fără a modifica codul existent.*  

---

### **3. Liskov Substitution Principle (LSP)**  
🔹 *Clasele derivate trebuie să poată fi folosite în locul claselor de bază fără a produce erori.*  

#### ❌ **Exemplu greșit**:
```python
class Dreptunghi:
    def __init__(self, latime, inaltime):
        self.latime = latime
        self.inaltime = inaltime

    def aria(self):
        return self.latime * self.inaltime

class Patrat(Dreptunghi):
    def __init__(self, latura):
        super().__init__(latura, latura)

dreptunghi = Dreptunghi(2, 3)
patrat = Patrat(5)

print(dreptunghi.aria())  # 6
print(patrat.aria())      # 25
```
*Deși funcționează, relația de moștenire poate duce la comportamente neașteptate dacă setăm `latime` sau `inaltime` separat.*

#### ✅ **Exemplu corect**:
```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def aria(self):
        pass

class Dreptunghi(Forma):
    def __init__(self, latime, inaltime):
        self.latime = latime
        self.inaltime = inaltime

    def aria(self):
        return self.latime * self.inaltime

class Patrat(Forma):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura ** 2

# Utilizare
forme = [Dreptunghi(2, 3), Patrat(5)]
for forma in forme:
    print(forma.aria())
```
*✔ Clasa `Patrat` nu mai depinde de `Dreptunghi` și respectă LSP.*  

---

### **4. Interface Segregation Principle (ISP)**  
🔹 *Nu forța o clasă să implementeze metode pe care nu le folosește.*  

#### ❌ **Exemplu greșit**:
```python
class Dispozitiv:
    def printeaza(self):
        pass

    def scaneaza(self):
        pass

class Imprimanta(Dispozitiv):
    def printeaza(self):
        print("Printez document.")

    def scaneaza(self):
        raise NotImplementedError("Această imprimantă nu poate scana.")
```
*Problema:* `Imprimanta` este forțată să implementeze `scaneaza()`.

#### ✅ **Exemplu corect**:
```python
class Printabil:
    def printeaza(self):
        pass

class Scanabil:
    def scaneaza(self):
        pass

class Imprimanta(Printabil):
    def printeaza(self):
        print("Printez document.")

class Scanner(Scanabil):
    def scaneaza(self):
        print("Scanez document.")

# Utilizare
imprimanta = Imprimanta()
imprimanta.printeaza()

scanner = Scanner()
scanner.scaneaza()
```
*✔ Fiecare clasă implementează doar ce are nevoie.*  

---

### **5. Dependency Inversion Principle (DIP)**  
🔹 *Modulele de nivel înalt nu trebuie să depindă de cele de nivel jos, ci de abstracții.*

#### ❌ **Exemplu greșit**:
```python
class MySQLDatabase:
    def conecteaza(self):
        print("Conectare la MySQL")

class Aplicatie:
    def __init__(self):
        self.db = MySQLDatabase()

    def porneste(self):
        self.db.conecteaza()
```
*Problema:* `Aplicatie` depinde direct de `MySQLDatabase`.

#### ✅ **Exemplu corect**:
```python
from abc import ABC, abstractmethod

class BazaDeDate(ABC):
    @abstractmethod
    def conecteaza(self):
        pass

class MySQLDatabase(BazaDeDate):
    def conecteaza(self):
        print("Conectare la MySQL")

class PostgreSQLDatabase(BazaDeDate):
    def conecteaza(self):
        print("Conectare la PostgreSQL")

class Aplicatie:
    def __init__(self, db: BazaDeDate):
        self.db = db

    def porneste(self):
        self.db.conecteaza()

# Utilizare
app = Aplicatie(PostgreSQLDatabase())
app.porneste()
```
*✔ Codul este flexibil și poate folosi orice tip de bază de date care respectă interfața `BazaDeDate`.*  

---

### References

https://en.wikipedia.org/wiki/SOLID
