import unittest
from src.game import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game("Player 1", "Rock")

    def test_has_player_name(self):
        self.assertEqual("Player 1", self.game.name)

    def test_has_choice(self):
        self.assertEqual("Rock", self.game.choice)

    def test_game_tie(self):
        p1 = Game("Player 1", "Rock")
        p2 = Game("Player 2", "Rock")
        self.assertEqual("It's a Tie!", self.game.play_game(p1, p2))

    def test_game_rock_wins(self):
        p1 = Game("Player 1", "Rock")
        p2 = Game("Player 2", "Scissors")
        self.assertEqual("Player 1 wins!", self.game.play_game(p1, p2))

    def test_game_scissors_wins(self):
        p1 = Game("Player 1", "Paper")
        p2 = Game("Player 2", "Scissors")
        self.assertEqual("Player 2 wins!", self.game.play_game(p1, p2))

    def test_game_rock_wins(self):
        p1 = Game("Player 1", "Wood")
        p2 = Game("Player 2", "Stone")
        self.assertEqual("Please input Rock, Paper, or Scissors!", self.game.play_game(p1, p2))
    