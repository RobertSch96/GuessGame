# This is a guess the number game
import random
import string
import sys
import _tkinter
from tokenize import Number
import streamlit as st

st.text('Thanks for Trying!')
st.caption('Im a noob...')
st.title('GuessGame')
st.header('Guess The Number')
st.subheader('Have fun!')


st.write("Hello friend!")
if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

def disable():
    st.session_state["disabled"] = True

name  = st.text_input(
    "What is your name?", 
    disabled=st.session_state.disabled, 
    on_change=disable
)

if name:
    st.write("Well " + name + " i am thinking of a number between 1- 20")
    st.write("Take a guess")

Coin = 25
st.write("you have " + str(Coin) + " Coins!")

lol = random.randint(1,200)


a = st.number_input("Number between 1-20",value=0)
if Coin == 0:
     st.write("Youre out of Coins! Please purchase more Coins")


def game(Coin):
    Attempts = 6
    secretnumber = random.randint(1,20)
    for Attempts in range(1-7):       
        if a == 0:
            st.write("")               
        elif a != secretnumber:
            if a > secretnumber:
                st.write('Incorrect! Your guess was too high!')
                st.write("Take another guess!")
                Attempts = Attempts - 1
                st.write("you have " + str(Attempts)+ " Attempts left")
                Coin = Coin-1
                st.write("You have " + str(Coin) + " Coins left")
            elif a < secretnumber:
                    st.write("Incorrect! Your guess was too low")
                    st.write("Take another guess!")
                    Attempts = Attempts - 1
                    st.write("you have " + str(Attempts)+ " Attempts left")
                    Token = Coin-1
                    st.write("You have " + str(Coin) + " Coins left")
        else:
                st.write('You guessed correctly!')
                st.write("The Secret Number was " +str(secretnumber))
                st.write("you had " + str(Attempts)+ " Attempts left")
                Token = Coin + 5
                st.write("You have " + str(Coin) + " Coins left")
                break
        return Coin
            
Coin = game(a)
   



#st.write("The Secret Number was " +str(secretnumber ))


    
    