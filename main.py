# This is a guess the number game
from multiprocessing.sharedctypes import Value
import random
import sys
import _tkinter
import streamlit as st
print("Hello, what is your name?")
name = input()

print("Well" + name + " i am thinking of a number between 1- 20")
secretnumber = random.randint(1,20)
try:
    for guessesTaken in range(1,7):
        print("Take a guess")
        guess = int(st.text_input())
        if guess == secretnumber:
            print("You guessed correctly!")
            break
        elif guess != secretnumber:
            if guess > secretnumber:
                print("Incorrect! Your guess was too high!")
                print("Take another guess!")
            elif guess < secretnumber:
                print("Incorrect! Your guess was too low")
                print("Take another guess!")
except:ValueError
print("You did not enter a number")
   



print("The Secret Number was " +str(secretnumber ))
print("you took " + str(guessesTaken) + " guesses")

    
    