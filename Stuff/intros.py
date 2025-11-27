#! python3
from tkinter import *
from tkinter import ttk

import os
import urllib.request
import urllib.parse

from math import ceil
from time import sleep

from common import InstructionsFrame
from gui import GUI

from constants import URL


################################################################################
# TEXTS
intro = """Welcome to the next part of the study.

In this part, you will first receive a short general knowledge quiz. Then you will answer questions regarding your attitudes and opinions. This part should take approximately 5-10 minutes.

Press the "Continue" button."""


ending = """This was the last task of the study.

The results of the experiment will be freely available on the Decision Lab website at the Faculty of Business Administration shortly after data evaluation and publication of the results. We ask you not to disclose the details of this study to potential participants, so that their choices and answers are not influenced and invalidated.
  
You can take all your belongings, the completed payment document, and without disturbing other participants, go to the next room to the research assistant, from whom you will receive your reward. 

This is the end of the experiment. Thank you for your participation!
 
Decision Lab"""

################################################################################




class Ending(InstructionsFrame):
    def __init__(self, root):
        super().__init__(root, text = ending, proceed = False, keys = ["g", "G"], height = "auto", width = 80)
        self.file.write("Ending\n")
        self.file.write(self.id + "\n\n")

    def run(self):
        self.sendInfo()

    def sendInfo(self):
        while True:
            self.update()    
            data = urllib.parse.urlencode({'id': self.root.id, 'round': -99, 'offer': "999"})
            data = data.encode('ascii')
            if URL == "TEST":
                response = "ok"
            else:
                try:
                    with urllib.request.urlopen(URL, data = data) as f:
                        response = f.read().decode("utf-8") 
                except Exception:
                    pass
            if "ok" in response:                     
                break              
            sleep(5)

    def gothrough(self):
        self.run()
        super().gothrough()



Intro = (InstructionsFrame, {"text": intro, "proceed": True, "height": "auto"})


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.getcwd()))
    GUI([Intro,
         Ending])
