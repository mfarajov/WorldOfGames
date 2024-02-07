
class GameRegistry:
    games = {}
    next_game_number = 1

    @classmethod
    def register_game(cls, game_class):
        cls.games[cls.next_game_number] = game_class.__name__
        cls.next_game_number += 1






