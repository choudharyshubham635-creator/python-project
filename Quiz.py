import streamlit as str

str.write('Hello, I am shubham welcome to my quiz zone.. hope you like the game. you my please proceed further for gaming...')
age = str.number_input('Enter ur Age....')
if age>=18:
  str.write("You are eligible for licence...")
  str.balloons()
 # str.snow()
else:
  str.write('You are not eligible...')
