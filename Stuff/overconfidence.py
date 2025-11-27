#! python3
from tkinter import *
from tkinter import ttk
from collections import deque
from time import perf_counter, sleep

import random
import os

from common import ExperimentFrame, InstructionsFrame
from gui import GUI
from constants import TESTING





question1 = "How many out of the ten questions do you think you answered correctly?"
question2 = """How do you think your performance on this test compares to that of other participants in this study?

Please estimate your percentile score by entering a number from 0 to 99, where:
• 0 means you performed worse than all other participants
• 99 means you performed better than all other participants  
• 50 represents the average performance of all participants"""



class Overconfidence(ExperimentFrame):
    def __init__(self, root):
        super().__init__(root)

        self.file.write("Overconfidence\n")

        self.firstAnswerVar = StringVar()
        self.secondAnswerVar = StringVar()

        ttk.Style().configure("TButton", font = "helvetica 15")

        # Question 1
        self.question1Frame = Canvas(self, background = "white", highlightbackground = "white", highlightcolor = "white")
        self.question1Frame.grid(row = 1, column = 1, pady = 20)

        self.question1Text = Text(self.question1Frame, font = "helvetica 15", relief = "flat", background = "white",
                         width = 80, height = 2, pady = 7, wrap = "word")
        self.question1Text.grid(row = 0, column = 1, columnspan = 2, sticky = S, pady = 10)
        self.question1Text.tag_configure("center", justify = "center")
        self.question1Text.insert("1.0", question1, "center")
        self.question1Text["state"] = "disabled"

        self.answer1Entry = ttk.Entry(self.question1Frame, textvariable = self.firstAnswerVar, font = "helvetica 15", width = 10)
        self.answer1Entry.grid(row = 1, column = 1, columnspan = 2, pady = 10)

        self.warning1 = ttk.Label(self.question1Frame, text = "Please enter an integer between 0 and 10", 
                                 font = "helvetica 13", background = "white", foreground = "white", justify = "center")
        self.warning1.grid(row = 2, column = 1, columnspan = 2, pady = 5)

        self.next1 = ttk.Button(self.question1Frame, text = "Continue", command = self.validateQuestion1)
        self.next1.grid(row = 3, column = 1, columnspan = 2, pady = 10)

        # Question 2 (initially hidden)
        self.question2Frame = Canvas(self, background = "white", highlightbackground = "white", highlightcolor = "white")
        
        self.question2Text = Text(self.question2Frame, font = "helvetica 15", relief = "flat", background = "white",
                         width = 80, height = 7, pady = 7, wrap = "word")
        self.question2Text.grid(row = 0, column = 1, columnspan = 2, sticky = S, pady = 10)
        self.question2Text.tag_configure("center", justify = "center")
        self.question2Text.insert("1.0", question2, "center")
        self.question2Text["state"] = "disabled"

        self.answer2Entry = ttk.Entry(self.question2Frame, textvariable = self.secondAnswerVar, font = "helvetica 15", width = 10)
        self.answer2Entry.grid(row = 1, column = 1, columnspan = 2, pady = 10)

        self.warning2 = ttk.Label(self.question2Frame, text = "Please enter an integer between 0 and 99", 
                                 font = "helvetica 13", background = "white", foreground = "white", justify = "center")
        self.warning2.grid(row = 2, column = 1, columnspan = 2, pady = 5)

        self.next2 = ttk.Button(self.question2Frame, text = "Continue", command = self.validateQuestion2)
        self.next2.grid(row = 3, column = 1, columnspan = 2, pady = 10)

        # Invisible spacer to reserve space for question 2 (prevents question 1 from moving)
        self.spacer = Canvas(self, background = "white", highlightbackground = "white", 
                            highlightcolor = "white", height = 350, width = 1)
        self.spacer.grid(row = 1, column = 1, pady = 20, sticky = W)
        self.spacer2 = Canvas(self, background = "white", highlightbackground = "white", 
                            highlightcolor = "white", height = 350, width = 1)
        self.spacer2.grid(row = 2, column = 1, pady = 20, sticky = W)

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(2, weight = 1)
        
        self.rowconfigure(0, weight = 1)
        #self.rowconfigure(1, weight = 1)
        #self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)


    def validateQuestion1(self):
        try:
            answer = int(self.firstAnswerVar.get())
            if answer < 0 or answer > 10:
                self.warning1["foreground"] = "red"
                return
        except:
            self.warning1["foreground"] = "red"     
            return
        
        # Valid answer - hide warning and show question 2
        self.warning1["foreground"] = "white"
        self.next1["state"] = "disabled"
        
        # Disable question 1 entry
        self.answer1Entry["state"] = "disabled"
        
        # Hide spacer and show question 2 frame
        self.spacer.grid_forget()
        self.question2Frame.grid(row = 2, column = 1, pady = 20)


    def validateQuestion2(self):
        try:
            answer = int(self.secondAnswerVar.get())
            if answer < 0 or answer > 99:
                self.warning2["foreground"] = "red"
                return
        except:
            self.warning2["foreground"] = "red"     
            return
        
        # Valid answer - proceed
        self.warning2["foreground"] = "white"
        
        # Write results to file
        self.file.write(self.id + "\t" + self.firstAnswerVar.get() + "\t" + self.secondAnswerVar.get() + "\n\n")
        
        # Continue to next frame
        self.nextFun()






if __name__ == "__main__":
    os.chdir(os.path.dirname(os.getcwd()))
    GUI([Overconfidence])

