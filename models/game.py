class Game():

    def game(self, player_1_choice, player_2_choice):
        if player_1_choice == "rock" and player_2_choice == "paper":
            return "Player 2 wins choosing paper"
        if player_1_choice == "rock" and player_2_choice == "scissors":
            return "Player 1 wins choosing rock"
        if player_1_choice == "paper" and player_2_choice == "rock":
            return "Player 1 wins chosing paper"
        if player_1_choice == "paper" and player_2_choice == "scissors":
            return "Player 2 wins choosing scissors"
        if player_1_choice == "scissors" and player_2_choice == "paper":
            return "Player 1 wins choosing scissors"
        if player_1_choice == "scissors" and player_2_choice == "rock":
            return "Player 2 wins choosing rock"
        if player_1_choice == player_2_choice:
            return None