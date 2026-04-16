import random
import string


class TOH:
    def __init__(self, difficulty):
        if difficulty > 10 or difficulty < 3:
            raise ValueError("Incorrect Difficulty. Please provide a number between 3 and 10.")
        self.size = difficulty
        self.towers = [list(range(self.size, 0, -1)), [], []]
        self._moves = 0

    # --- Core Methods ---

    def move(self, from_tower, to_tower):
        if self.valid_move(from_tower, to_tower):
            print(f"Moving disc from tower {from_tower} to tower {to_tower}\n")
            self.towers[to_tower].append(self.towers[from_tower].pop())
            self._moves += 1
            self.render()
        else:
            print("Invalid Move")

    def valid_move(self, from_tower, to_tower):
        if from_tower not in range(3):
            return False
        if to_tower not in range(3):
            return False
        if len(self.towers[from_tower]) == 0:
            return False
        if len(self.towers[to_tower]) == 0:
            return True
        return self.towers[from_tower][-1] < self.towers[to_tower][-1]

    def render(self):
        size_arr = []
        for num in range(self.size + 2):
            if num == 0:
                size_arr.append(" " * (self.size + 2) + "||" + " " * (self.size + 2))
            elif num == self.size + 1:
                size_arr.append(" " + "=" * ((self.size + 2) * 2) + " ")
            else:
                str1 = "  " + " " * (self.size - num) + "*" * num
                str2 = "*" * num + " " * (self.size - num) + "  "
                size_arr.append(str1 + "**" + str2)

        output = []
        output.append(size_arr[0] * 3)

        for num in range(self.size - 1, -1, -1):
            row = ""
            for tower in self.towers:
                disc = tower[num] if num < len(tower) else 0
                row += size_arr[disc]
            output.append(row)

        output.append(size_arr[self.size + 1] * 3)

        for line in output:
            print(line)
        print()

    def won(self):
        return len(self.towers[1]) == self.size or len(self.towers[2]) == self.size

    # --- Gameplay Loop ---

    def play(self):
        letter = random.choice(string.ascii_uppercase)
        print("\n\nWelcome back to another exciting game of Towers of Hanoi!")
        print(f"This game is brought to you by the letter '{letter}'\n")
        print(f"This game's difficulty is set to {self.size}")
        print("Move discs by entering which tower you would like to take from and where you would like to place it.")
        print("Type 'quit' at any time to exit the game")
        print("Good luck and have fun!\n")
        self.render()

        while not self.won():
            user_input = input("Enter in your move (Ex: '0 1'): ").strip()
            if user_input.lower() == "quit":
                return "Quitting the game..."
            parts = user_input.split()
            if len(parts) != 2:
                print("Invalid input length")
                continue
            try:
                from_t, to_t = int(parts[0]), int(parts[1])
            except ValueError:
                print("Invalid input. Please enter two numbers.")
                continue
            self.move(from_t, to_t)

        print("You've solved the puzzle!\nCongratulations!")
        print(f"It took you {self._moves} moves")
        optimal = 2 ** self.size - 1
        if self._moves == optimal:
            print("This was an optimal solution. Great Job!")
        else:
            print(f"The optimal solution for this difficulty is {optimal} moves.")
        return "YOU WIN!"


if __name__ == "__main__":
    try:
        difficulty = int(input("Enter a difficulty (3 - 10): "))
        game = TOH(difficulty)
        result = game.play()
        print(result)
    except ValueError as e:
        print(e)
