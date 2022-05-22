class Game:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def play_game(self, p1, p2):
        if p1.choice == p2.choice:
            return "It's a Tie!"
        elif p1.choice ==  "Rock" and p2.choice == "Scissors":
            return "Player 1 wins!"
        elif p1.choice == "Scissors" and p2.choice == "Rock":
            return "Player 2 wins!"
        elif p1.choice == "Rock" and p2.choice == "Paper":
            return "Player 2 wins!"
        elif p1.choice == "Paper" and p1.choice == "Rock":
            return "Player 1 wins!"
        elif p1.choice == "Scissors" and p2.choice == "Paper":
            return "Player 1 wins!"
        elif p1.choice == "Paper" and p2.choice == "Scissors":
            return "Player 2 wins!"
        else:
            return "Please input Rock, Paper, or Scissors!"
