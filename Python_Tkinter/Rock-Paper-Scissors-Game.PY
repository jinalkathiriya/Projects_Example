import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.choices = ['Rock', 'Paper', 'Scissors']
        self.user_score = 0
        self.computer_score = 0

        self.title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 20))
        self.title_label.pack(pady=10)

        self.choice_label = tk.Label(root, text="Choose your move:", font=("Arial", 14))
        self.choice_label.pack(pady=5)

        self.choice_var = tk.StringVar()
        self.choice_var.set(self.choices[0])

        self.choice_menu = ttk.Combobox(root, textvariable=self.choice_var, values=self.choices)
        self.choice_menu.pack(pady=5)

        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="User: 0  Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

        self.thinking_label = tk.Label(root, text="", font=("Arial", 14))
        self.thinking_label.pack(pady=5)

    def play(self):
        user_choice = self.choice_var.get()

        self.play_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.DISABLED)
        self.thinking_label.config(text="Computer is thinking...")
        
        # Start the thinking animation
        self.root.after(500, lambda: self.thinking_animation(user_choice))

    def thinking_animation(self, user_choice):
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")
        self.play_again_button.config(state=tk.NORMAL)
        self.play_button.config(state=tk.DISABLED)
        self.thinking_label.config(text="")

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == 'Rock' and computer == 'Scissors') or (user == 'Scissors' and computer == 'Paper') or (user == 'Paper' and computer == 'Rock'):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def reset_game(self):
        self.result_label.config(text="")
        self.choice_var.set(self.choices[0])
        self.play_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)
        self.thinking_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
