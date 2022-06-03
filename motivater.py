import streamlit as sl
import random
sl.header('Welcome to Rattle Motivater')
sl.write('Welcome to Rattle Motivater!You can use it to motivate yourself.')
if sl.button('Motivate me!'):
    m={1:"Success is not final;Failure is not fatal:it is the courage to continue that counts",2:"Out of the mountain of despair,a stone of hope -Martin luther king,Jr.",3:"Education is the vaccine for the violence",4:"Believe in yourself and anything is possible",5:"Every day is a chance to be better",6:"Don't stop until you're proud",7:"Success is not an activity but a progress",8:"You must be the change you want to see in the world-Mahatma Gandhi"}
    r=random.randint(1,6)

    sl.header(m[r])
