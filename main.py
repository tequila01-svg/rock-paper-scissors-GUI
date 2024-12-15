import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        master.geometry("400x500")
        master.configure(bg='#f0f0f0')

        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0

        # Title
        self.title_label = tk.Label(
            master, 
            text="Rock Paper Scissors", 
            font=("Arial", 20, "bold"), 
            bg='#f0f0f0', 
            fg='#333333'
        )
        self.title_label.pack(pady=20)

        # Score Frame
        self.score_frame = tk.Frame(master, bg='#f0f0f0')
        self.score_frame.pack(pady=10)

        self.player_score_label = tk.Label(
            self.score_frame, 
            text=f"Player: {self.player_score}", 
            font=("Arial", 14), 
            bg='#f0f0f0'
        )
        self.player_score_label.pack(side=tk.LEFT, padx=10)

        self.computer_score_label = tk.Label(
            self.score_frame, 
            text=f"Computer: {self.computer_score}", 
            font=("Arial", 14), 
            bg='#f0f0f0'
        )
        self.computer_score_label.pack(side=tk.LEFT, padx=10)

        # Choice Frame
        self.choice_frame = tk.Frame(master, bg='#f0f0f0')
        self.choice_frame.pack(pady=20)

        self.choices = ['Rock', 'Paper', 'Scissors']
        self.choice_buttons = []

        for choice in self.choices:
            button = tk.Button(
                self.choice_frame, 
                text=choice, 
                command=lambda c=choice: self.play_game(c),
                width=10,
                font=("Arial", 12),
                bg='#4CAF50',
                fg='white'
            )
            button.pack(side=tk.LEFT, padx=10)
            self.choice_buttons.append(button)

        # Result Label
        self.result_label = tk.Label(
            master, 
            text="Make your choice!", 
            font=("Arial", 16), 
            bg='#f0f0f0', 
            fg='#333333'
        )
        self.result_label.pack(pady=20)

    def play_game(self, player_choice):
        # Computer makes a random choice
        computer_choice = random.choice(self.choices)

        # Determine the winner
        result = self.determine_winner(player_choice, computer_choice)

        # Update scores
        if result == "Player Wins!":
            self.player_score += 1
        elif result == "Computer Wins!":
            self.computer_score += 1

        # Update labels
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
        
        # Update result label
        self.result_label.config(
            text=f"You chose {player_choice}, Computer chose {computer_choice}. {result}"
        )

        # Increment rounds
        self.rounds_played += 1

        # Check for game end (optional - set to 5 rounds)
        if self.rounds_played == 5:
            self.end_game()

    def determine_winner(self, player_choice, computer_choice):
        # Game logic to determine winner
        if player_choice == computer_choice:
            return "It's a Tie!"
        
        # Winning combinations
        wins = {
            'Rock': 'Scissors',
            'Paper': 'Rock',
            'Scissors': 'Paper'
        }

        if wins[player_choice] == computer_choice:
            return "Player Wins!"
        else:
            return "Computer Wins!"

    def end_game(self):
        # Disable buttons
        for button in self.choice_buttons:
            button.config(state=tk.DISABLED)

        # Determine overall winner
        if self.player_score > self.computer_score:
            winner = "Player"
        elif self.player_score < self.computer_score:
            winner = "Computer"
        else:
            winner = "Nobody (It's a Tie)"

        # Show game over message
        messagebox.showinfo(
            "Game Over", 
            f"Game finished!\n\n"
            f"Final Score:\n"
            f"Player: {self.player_score}\n"
            f"Computer: {self.computer_score}\n\n"
            f"Overall Winner: {winner}"
        )

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()