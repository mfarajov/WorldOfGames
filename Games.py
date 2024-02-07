from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    @abstractmethod
    def display_welcome_message(self):
        pass

    @abstractmethod
    def end_game(self):
        pass





