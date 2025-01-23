import tkinter as tk
from tkinter import ttk, messagebox
import random
from PIL import Image, ImageTk  

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")

        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds = 0

        self.options = ["rock", "paper", "scissors"]

        # Load images using Pillow
        self.images = {
            "rock": ImageTk.PhotoImage(Image.open("C:/Web Development/rock.png").resize((50, 50))),
            "paper": ImageTk.PhotoImage(Image.open("C:/Web Development/paper.png").resize((50, 50))),
            "scissors": ImageTk.PhotoImage(Image.open("C:/Web Development/scissor.png").resize((50, 50)))
        }

        self.create_widgets()

    def create_widgets(self):
        font_style = ("Arial", 14)

        # Buttons with icons
        ttk.Button(
            self.root,
            text="Rock",
            image=self.images["rock"],
            compound=tk.LEFT,
            command=lambda: self.play_round("rock")
        ).pack(pady=10)

        ttk.Button(
            self.root,
            text="Paper",
            image=self.images["paper"],
            compound=tk.LEFT,
            command=lambda: self.play_round("paper")
        ).pack(pady=10)

        ttk.Button(
            self.root,
            text="Scissors",
            image=self.images["scissors"],
            compound=tk.LEFT,
            command=lambda: self.play_round("scissors")
        ).pack(pady=10)

        # Labels
        self.result_label = ttk.Label(self.root, text="Make your move!", font=("Arial", 16))
        self.result_label.pack(pady=20)

        self.score_label = ttk.Label(self.root, text="Player: 0 | Computer: 0 | Ties: 0", font=font_style)
        self.score_label.pack(pady=10)

        self.round_label = ttk.Label(self.root, text="Rounds Played: 0", font=font_style)
        self.round_label.pack(pady=10)

        # Reset button
        ttk.Button(self.root, text="Reset Game", command=self.reset_game).pack(pady=10)

        # Instructions
        ttk.Button(self.root, text="Instructions", command=self.show_instructions).pack(pady=10)

        # Exit button
        ttk.Button(self.root, text="Exit", command=self.on_exit).pack(pady=10)

    def play_round(self, player_choice):
        computer_choice = random.choice(self.options)
        self.rounds += 1

        if player_choice == computer_choice:
            self.result_label.config(text=f"It's a Tie! Both chose {player_choice}")
            self.ties += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.result_label.config(text=f"You Win! {player_choice} beats {computer_choice}")
            self.player_score += 1
        else:
            self.result_label.config(text=f"Computer Wins! {computer_choice} beats {player_choice}")
            self.computer_score += 1

        self.update_scores()

    def update_scores(self):
        self.score_label.config(text=f"Player: {self.player_score} | Computer: {self.computer_score} | Ties: {self.ties}")
        self.round_label.config(text=f"Rounds Played: {self.rounds}")

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds = 0

        self.result_label.config(text="Make your move!")
        self.update_scores()

    def show_instructions(self):
        instructions_text = (
            "Welcome to Rock, Paper, Scissors!\n\n"
            "Choose Rock, Paper, or Scissors to play.\n"
            "The system will randomly select one, and the winner is determined as follows:\n"
            "- Rock beats Scissors\n"
            "- Scissors beats Paper\n"
            "- Paper beats Rock\n\n"
            "The game keeps track of your score and the computer's score."
        )
        messagebox.showinfo("Instructions", instructions_text)

    def on_exit(self):
        if messagebox.askyesno("Exit Game", "Are you sure you want to exit?"):
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
