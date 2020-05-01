'''
James Volino
chooseperson.py

This program will allow the user to click a button and a random name will appear and will contnue to randomly choose until program is closed

'''
#Import statement for GUI and random
from breezypythongui import EasyFrame
import random

class RandomPerson(EasyFrame):
#Allows the user to click the displayed button and allow it to display a random name
    def __init__(self):
        #Sets up windows and widgets
        EasyFrame.__init__(self, "Who will win?", background = "skyblue", height = 125, width = 300)
        self.addLabel(text = "And the winner is...", row = 0, column = 0, sticky = "NSEW", background = "skyblue", foreground = "black")
        self.addButton(text = "Lets go!", row = 1, column = 0, columnspan = 2, command = self.studentChoice)
        self.previousWinner = ""
    
    def studentChoice(self):
    #Runs the button command studentChoice()
        studentList = ["Don Johnson", "Johnny Drama", "Turtle", "Michael Scott", "Dwight Shrute", "Steven Hyde", "Red Foreman"]
        self.studentList = random.choice(studentList)
        winner = self.studentList
        #while loop to ensure that a name doesnt repeat twice
        while winner == self.previousWinner:
            self.studentList = random.choice(studentList)
            
        #Prints the winner to a message box on click of the button
        self.messageBox(title = "Winner", message = winner + "!")
        
#Global defintion of main to run the class
def main():
    RandomPerson().mainloop()
#Global call to the main function
main()