from Live import welcome, load_game
from MemoryGame import *
from GuessGame import *
from CurrencyRouletteGame import *
import os


def get_input(env_var, prompt, cast_type=str):
    value = os.getenv(env_var)
    if value is None:
        value = input(prompt)
    return cast_type(value)


def main():
    # player_name = input("Please enter your name: ")
    player_name = get_input("PLAYER_NAME", "Please enter your name: ")
    welcome(player_name)
    difficulty_levels = range(1, 10)
    load_game(GameRegistry.games, difficulty_levels)


if __name__ == "__main__":
    main()
