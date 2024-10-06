import random

class MathTutor:
    def __init__(self):
        # Definim operațiile matematice folosind funcții lambda
        self.operations = [
            (lambda a, b: a + b, "Adunare", "+"),
            (lambda a, b: a - b, "Scădere", "-"),
            (lambda a, b: a * b, "Înmulțire", "*"),
            (lambda a, b: a // b if b != 0 else None, "Împărțire", "/")
        ]

    def practice_session(self):
        score = 0
        total_questions = 5

        for i in range(total_questions):
            op, op_name, op_symbol = random.choice(self.operations)
            a = random.randint(1, 10)
            b = random.randint(1, 10)

            print(f"\nÎntrebarea {i+1}: {a} {op_symbol} {b} = ?")

            correct_answer = op(a, b)
            if correct_answer is None:
                print("Atenție: Împărțire la zero! Vom genera o altă întrebare.")
                continue

            try:
                user_answer = int(input("Răspunsul tău: "))
                if user_answer == correct_answer:
                    print("Corect!")
                    score += 1
                else:
                    print(f"Incorect. Răspunsul corect este: {correct_answer}")
            except ValueError:
                print("Te rog să introduci un număr valid.")

        print(f"\nSesiune încheiată. Scorul tău: {score}/{total_questions}")

def main():
    tutor = MathTutor()
    print("Bine ați venit la sesiunea de practică matematică!")
    tutor.practice_session()

if __name__ == "__main__":
    main()
