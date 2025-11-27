#! python3

import sys
import os
import argparse

sys.path.append(os.path.join(os.getcwd(), "Stuff"))


from gui import GUI

from quest import Mindset
from intros import Intro, Ending
from demo import Demographics
from login import Login
from overconfidence import Overconfidence
from quiz import Quiz

frames = [Login,
          Intro,   
          Mindset,  
          Quiz,     
          Overconfidence,          
          Demographics,
          Ending
         ]



def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Run experiment')
    parser.add_argument('--load', type=str, default='True', help='Load previous session data')    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    if args.load == "False":
        load = False
    else:
        load = os.path.exists("temp.json")    
    
    GUI(frames, load=load)