import random
import time
from Games import Game
from GameRegistry import GameRegistry
import os
from inputs import get_input


class MemoryGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)

    def display_welcome_message(self):
        print('Welcome to the Memory Game!')

    def end_game(self):
        print('Memory Game ended!')

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        print(f"Enter {self.difficulty} numbers separated by spaces:")
        # return [int(x) for x in input().split()]
        return get_input("USER_SEQUENCE", "Enter the sequence you remember: ", lambda x: [int(num) for num in x.split(" ")])

    @staticmethod
    def is_list_equal(list1, list2):
        return list1 == list2

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def play(self):
        sequence = self.generate_sequence()
        print("Remember these numbers: ")
        print(sequence)
        time.sleep(0.7)
        self.clear_screen()
        user_sequence = self.get_list_from_user()
        print('Number list was: ', sequence)
        if self.is_list_equal(sequence, user_sequence):
            print('Congratulations! You won the Memory Game!')
        else:
            print('Unfortunately You lost the Memory Game!')


GameRegistry.register_game(MemoryGame)


