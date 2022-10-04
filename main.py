# This is a guess the number game
from multiprocessing.sharedctypes import Value
import random
import sys
import _tkinter
import streamlit as st

st.text('Thanks for Trying!')
st.caption('Im a noob...')
st.title('GuessGame')
st.header('Guess The Number')
st.subheader('Have fun!')


st.write("Hello, what is your name?")
name = st.text_input(label="Your Name Here")

st.write("Well " + name + " i am thinking of a number between 1- 20")
#secretnumber = random.randint(1,20)
st.write("Take a guess")

#def ggame(a):

secretnumber = random.randint(1,20)
lol = random.randint(1,200)
a = st.number_input("number goes here", key=lol)
if a > secretnumber:
    st.write("Your number is greater than 20!")
elif a == secretnumber:
    st.write('You guessed correctly!')
    st.write("The Secret Number was " +str(secretnumber))
elif a != secretnumber:
    if a > secretnumber:
      st.write('Incorrect! Your guess was too high!')
      st.write("Take another guess!")
elif a < secretnumber:
    st.write("Incorrect! Your guess was too low")
    st.write("Take another guess!")
            

   



#st.write("The Secret Number was " +str(secretnumber ))


    
    