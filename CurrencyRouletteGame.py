from Games import Game
from GameRegistry import GameRegistry
import random
from inputs import get_input


class CurrencyRouletteGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.current_rate = None  # Placeholder for the current exchange rate

    def display_welcome_message(self):
        print('Welcome to the Currency Roulette Game!')

    def end_game(self):
        print('Currency Roulette Game ended!')

    def get_money_interval(self, amount_in_usd):
        # Placeholder for getting the current exchange rate from an API
        # self.current_rate = currency_api_module.get_current_rate('USD', 'ILS')
        self.current_rate = 3.5  # Example rate, replace with actual API call

        total_value = amount_in_usd * self.current_rate
        return (total_value - (5 - self.difficulty),
                total_value + (5 - self.difficulty))

    @staticmethod
    def get_guess_from_user(amount_in_usd):
        print(f"How much do you think {amount_in_usd} USD is in ILS?")
        # return float(input("Enter your guess: "))
        return get_input('CURRENCY_GUESS', "Enter your guess: ", float)

    def play(self):
        amount_in_usd = random.randint(1, 100)
        interval = self.get_money_interval(amount_in_usd)
        user_guess = self.get_guess_from_user(amount_in_usd)
        if interval[0] <= user_guess <= interval[1]:
            print('Congratulations, You won!')
            return True
        else:
            print('Unfortunately You lost!')
            print(f'Approximate amount is supposed to be between {interval[0]} and {interval[1]}')
            return False


GameRegistry.register_game(CurrencyRouletteGame)
