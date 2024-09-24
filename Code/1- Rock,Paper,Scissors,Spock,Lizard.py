import random
import tkinter as tk
from tkinter import messagebox

# Helper functions
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return None

# Game logic
def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    
    if player_number == -1:
        messagebox.showerror("Error", "Invalid choice!")
        return
    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    
    result_text = f"Player chooses {player_choice}\nComputer chooses {comp_choice}\n"
    
    diff = (comp_number - player_number) % 5
    if diff == 1 or diff == 2:
        result_text += "Computer Wins!"
    elif diff == 3 or diff == 4:
        result_text += "Player Wins!"
    else:
        result_text += "It's a tie!"
    
    result_label.config(text=result_text)

# Event handler for button click
def on_button_click(choice):
    rpsls(choice)

# Create the main window
window = tk.Tk()
window.title("Rock-paper-scissors-lizard-Spock")
window.minsize(600,400)

# Instruction label
instruction_label = tk.Label(window, text="Choose one:", font=('Helvetica', 14))
instruction_label.pack(pady=10)

# Buttons for each choice
choices = ["rock", "Spock", "paper", "lizard", "scissors"]
for choice in choices:
    button = tk.Button(window, text=choice, width=20, font=('Helvetica', 12), command=lambda c=choice: on_button_click(c))
    button.pack(pady=5)

# Result label
result_label = tk.Label(window, text="", font=('Helvetica', 14))
result_label.pack(pady=20)

# Run the window loop
window.mainloop()
