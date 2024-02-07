import os

def welcome(name):
    print(f"Welcome to the World of Games (WoG), {name}.\nHere you can find many cool games to play.")


def load_game(games, difficulties):

    for i, game in games.items():
        print(f"{i}. {game}")

    while True:
        try:
            if 'JENKINS_URL' in os.environ:
                game_choice = int(input("Enter your choice game (number): "))
            else:
                game_choice = int(os.getenv('GAME_CHOICE', '1'))
            if 1 <= game_choice <= len(games):
                break
            else:
                print("Invalid choice. Please choose a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            difficulty = int(input(f"Please choose game difficulty from 1 to {len(difficulties)}: "))
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
    game_instance.play()
    game_instance.end_game()

    return games[game_choice], difficulty























