# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import tkinter as tk
from tkinter import messagebox


#------------------------------------------
# declaring global variables
secret_number = 0
num_range = 100
remaining_guesses = 0

#------------------------------------------
# helper function to start and restart the game

def new_game():
    global secret_number, remaining_guesses,num_range
    print("----------------------------------------")
    print("New game. Range is from 0 to", num_range)
    
    secret_number = random.randrange(0, num_range)

    remaining_guesses = int( math.ceil(math.log(num_range, 2)) )
    
    print("Total Guesses:", remaining_guesses)
    
    
#------------------------------------------
# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 

    global num_range
    num_range = 100
    new_game()
    
  
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global num_range
    num_range = 1000
    new_game()
    

def reset():
    new_game()
    
    
def input_guess():
    
    global remaining_guesses, secret_number
    
    guess = int(guess_entry.get())
    
    print("Guess was", guess)
    
    if guess < secret_number:
        result_label.config(text="Higher!")
    elif guess > secret_number:
        result_label.config(text="Lower!")
    else:
        result_label.config(text="Correct!")
        new_game()
        return
    
    remaining_guesses -= 1
    remaining_guesses_label.config(text=f"Remaining Guesses: {remaining_guesses}")

    
    if remaining_guesses == 0:
        remaining_guesses_label.config(text=f"You ran out of guesses! : ( The number was {secret_number}. Starting a new game!)")
        new_game()

#------------------------------------------
        
# create frame

window = tk.Tk()
window.title("Guess the Number!")
window.minsize(400,400)

#------------------------------------------
range100_button = tk.Button(window,text="Range is [0, 100]",command=range100)
range100_button.pack(pady=5)

range1000_button = tk.Button(window,text="Range is [0, 1000]",command=range1000)
range1000_button.pack(pady=5)

reset_button = tk.Button(window,text="New Game",command=reset)
reset_button.pack(pady=5)

guess_entry_label = tk.Label(window,text="Enter your guess: ")
guess_entry_label.pack(pady=5)

guess_entry = tk.Entry(window)
guess_entry.pack(pady=5)

guess_button = tk.Button(window,text="Submit",command=input_guess)
guess_button.pack(pady=5)

# Label to display remaining guesses
remaining_guesses_label = tk.Label(window, text="Remaining guesses: ")
remaining_guesses_label.pack(pady=5)

# Label to display results (Higher, Lower, Correct)
result_label = tk.Label(window, text="")
result_label.pack(pady=5)
#------------------------------------------

new_game()

window.mainloop()




# always remember to check your completed program against the grading rubric
