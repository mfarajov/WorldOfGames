from Live import welcome, load_game
from MemoryGame import *
from GuessGame import *
from CurrencyRouletteGame import *
import os


def main():
    player_name = input("Please enter your name: ")
    # player_name = os.getenv('PLAYER_NAME', 'Murad Farajov')
    welcome(player_name)
    difficulty_levels = range(1, 100)
    load_game(GameRegistry.games, difficulty_levels)


if __name__ == "__main__":
    main()
