from random import *
from tkinter import *
import csv
from PIL import ImageTk, Image
import sys
import os


class Pokemon:
    def __init__(self,name):
        self.name = name

    #gets the Information from the CSV file
    def getInformation(self,x):
        with open('Pokemon.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == self.name:
                    return row[x]



# function to display data for a pokemon from tkinter
class GUI:
    def __init__(self,window):
        self.window = window
        window.title("Pokédex")
        window.configure(background="#CC0000")
        self.label = Label(window, text="Enter a Pokémon Name:", font=("Helvetica 15 bold"), fg="#ffffff", bg="#CC0000")
        self.label.pack()
        self.entry = Entry(window, bd =5, width=40)
        self.entry.pack()
        self.show_button = Button(window, text='Show',font=("Helvetica 10 bold"),  bg="#000000", fg="#ffffff" ,command=self.callPokedex)
        self.show_button.pack()

        self.reset = Button(window, text="Reset", font=("Helvetica 10 bold"),  bg="#000000", fg="#ffffff", command=self.resetPokedex)
        self.reset.pack()

        self.exit = Button(window, text="Exit", font=("Helvetica 10 bold"), bg="#000000", fg="#ffffff", command=self.exitPokedex)
        self.exit.pack()

    # Gets the pokemon information and prints it to the window
    def callPokedex(self):
        p1=Pokemon(self.entry.get())

        window.title("Pokédex -- Pokédemon Information")

        self.label2 = Label(window, text="Pokémon Number: "+p1.getInformation(0), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Name: "+p1.getInformation(1), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Type 1: "+p1.getInformation(2), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Type 2: "+p1.getInformation(3), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="HP: "+p1.getInformation(5), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Attack: "+p1.getInformation(6), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Defense: "+p1.getInformation(7), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Special Attack: "+p1.getInformation(8), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Special Defense: "+p1.getInformation(9), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Total: "+p1.getInformation(4), font=("Helvetica 10 bold"),fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Speed: "+p1.getInformation(10), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Generation: "+p1.getInformation(11), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()
        self.label2 = Label(window, text="Legendary: "+p1.getInformation(12), font=("Helvetica 10 bold"), fg="#ffffff", bg="#CC0000")
        self.label2.pack()

        result = p1.getInformation(0)

        path = ("C:/Users/Marlene/PycharmProjects/Pokedex/pokeimagini/" + result + ".png")
        im = Image.open(path)
        tkimage = ImageTk.PhotoImage(im)
        myvar = Label(window, image=tkimage)
        myvar.image = tkimage
        myvar.pack(side="bottom", fill="both", expand="yes")


    #reset the window function
    def resetPokedex(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    #exit the window function
    def exitPokedex(self):
        exit(0)

window = Tk(screenName="Pokédex")
pokedex = GUI(window)
window.mainloop()
