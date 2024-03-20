from inputs import get_input
from Score import add_score


def welcome(name):
    print(f"Welcome to the World of Games (WoG), {name}.\nHere you can find many cool games to play.")


def load_game(games, difficulties):

    for i, game in games.items():
        print(f"{i}. {game}")

    while True:
        try:
            # game_choice = int(input("Enter your choice game (number): "))
            game_choice = get_input("GAME_CHOICE", "Enter your choice game (number): ", int)
            if 1 <= game_choice <= len(games):
                break
            else:
                print("Invalid choice. Please choose a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            # difficulty = int(input(f"Please choose game difficulty from 1 to {len(difficulties)}: "))
            difficulty = get_input("DIFFICULTY", f"Please choose game difficulty from 1 to {len(difficulties)}: ", int)
            if 1 <= difficulty <= len(difficulties):
                break
            else:
                print(f"Invalid input. Please choose a difficulty level between 1 and {len(difficulties)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Playing {games[game_choice]} with difficulty level of {difficulty}")

    if games[game_choice] == 'MemoryGame':
        from MemoryGame import MemoryGame
        game_instance = MemoryGame(difficulty)

    elif games[game_choice] == 'GuessGame':
        from GuessGame import GuessGame
        game_instance = GuessGame(difficulty)

    elif games[game_choice] == 'CurrencyRouletteGame':
        from CurrencyRouletteGame import CurrencyRouletteGame
        game_instance = CurrencyRouletteGame(difficulty)

    game_instance.display_welcome_message()
    game_won = game_instance.play()
    game_instance.end_game()

    if game_won:
        add_score(difficulty)

    return games[game_choice], difficulty









