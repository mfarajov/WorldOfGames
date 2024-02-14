from Live import welcome, load_game
from MemoryGame import *
from GuessGame import *
from CurrencyRouletteGame import *


def main():
    player_name = get_input("PLAYER_NAME", "Please enter your name: ", str)
    welcome(player_name)
    difficulty_levels = range(1, 100)
    load_game(GameRegistry.games, difficulty_levels)


if __name__ == "__main__":
    main()
