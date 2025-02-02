import random

class game:
    def __init__(self, name, game_count):
        self.name = name
        self.game_count = game_count
        self.gss = int(0)
        self.numb = int(-1)
    def get_correct(self):
        try:
            return int(input("Take a guess.\n"))
        except:
            return print("Please enter integer")
    def get_checked(self):
        if self.numb < self.game_count:
            print("Your guess is too low.")
        elif self.numb > self.game_count:
            print("Your guess is too high.")

game = game(input("Hello! What is your name?\n"), random.randint(1, 20))

print( f"Well,{game.name}, I am thinking of a number between 1 and 20.")

while game.numb != game.game_count:
        game.numb = game.get_correct()
        game.gss += 1
        game.get_checked()


print(f"Good job, {game.name}! You guessed my number in {game.gss} guesses!")