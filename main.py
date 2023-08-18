# @mansourshebli

from tkinter import *
from tkinter import messagebox
import openai
import os
import sys
from tkcalendar import DateEntry

# Function to open the recommendation page
def open_recommendation_page():
    # Adding: Opening the recommendation page using the exec function
    exec(open('recommendation_page.py').read())

# Function to open the local tips page
def open_local_tips_page():
    # Adding: Opening the local tips page using the exec function
    exec(open('local_tips_page.py').read())

# Create the main window
window = Tk()
window.title('Tripify')
window.geometry('800x500')
window.config(bg='#00FFFF')

# Create a frame for the home screen content
home_frame = Frame(window, padx=50, pady=50, bg='#00FFFF')
home_frame.pack(expand=True)

# Adding: An emoji icon at the top
emoji_label = Label(home_frame, text='✈️', font=('Arial', 50), bg='#00FFFF')
emoji_label.pack()

# Adding: The app title
title_label = Label(home_frame, text='Tripify', font=('Helvetica', 24, 'bold'), bg='#00FFFF')
title_label.pack(pady=10)

# Creating: Button to navigate to the destination recommendations page
recommendation_button = Button(home_frame, text='Destination Recommendations', font=('Arial', 14, 'bold'), command=open_recommendation_page, bg='#FFD700', fg='black', pady=10)
recommendation_button.pack(pady=10, fill='x')

# Creating: Button to navigate to the local tips page
local_tips_button = Button(home_frame, text='Local Tips', font=('Arial', 14, 'bold'), command=open_local_tips_page, bg='#32CD32', fg='black', pady=10)
local_tips_button.pack(fill='x')

# Start the main event loop
window.mainloop()
