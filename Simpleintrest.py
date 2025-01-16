from tkinter import *
#from tkinter import tk

def calculate_simple_interest():

        simple_interest = (principal * time * rate) / 100

root = Tk()
root.title("Simple Intrest Calculator")
root.geometry("600x500")
       
principal = ("enter the principal amount")
time = ("Enter the time period:")
rate = (" Enter the rate")

principal= root.Label(root, text= "principal"  ("enter the principal amount:"))

root.mainloop()
