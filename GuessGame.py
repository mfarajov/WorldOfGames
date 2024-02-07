import random
from Games import Game
from GameRegistry import GameRegistry
from inputs import get_input


class GuessGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.secret_number = None

    def display_welcome_message(self):
        print('Welcome to the Guess Game!')

    def end_game(self):
        print('Guess Game ended!')

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                # user_guess = int(input(f"Enter a guess between 1 and {self.difficulty}: "))
                user_guess = get_input('USER_GUESS', f"Enter a guess between 1 and {self.difficulty}: ", int)
                if 1 <= user_guess <= self.difficulty:
                    return user_guess
                else:
                    print(f"Please enter a number within the range 1 to {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

    def compare_results(self, guess):
        return guess == self.secret_number

    def play(self):
        self.generate_number()
        user_guess = self.get_guess_from_user()
        print('Secret number was: ', self.secret_number)
        if self.compare_results(user_guess):
            print('Congratulations! You won the Guess Game!')
        else:
            print('Unfortunately You lost the Guess Game!')


GameRegistry.register_game(GuessGame)
