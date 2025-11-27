#! python3
from tkinter import *
from tkinter import ttk

import random
import os

from common import InstructionsAndUnderstanding
from gui import GUI


def parse_quiz(filename):
    """Parse quiz.txt and return list of [question, [answers], [feedback]]"""
    questions = []
    
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]
    
    current_question = None
    current_answers = []
    
    for line in lines:
        line = line.strip()
        if not line:  # Empty line - end of current question
            if current_question and current_answers:
                # Add question with empty feedback for each answer
                questions.append([current_question, current_answers, [""] * len(current_answers)])
                current_question = None
                current_answers = []
        elif line[0].isdigit() and '. ' in line:  # Question line (starts with number)
            # Extract question text (remove number and period)
            current_question = line.split('. ', 1)[1]
        elif line.startswith(('A)', 'B)', 'C)', 'D)')):  # Answer line
            # Extract answer text (remove letter and parenthesis)
            answer = line.split(') ', 1)[1] if ') ' in line else line[3:]
            current_answers.append(answer)
    
    # Add last question if file doesn't end with empty line
    if current_question and current_answers:
        questions.append([current_question, current_answers, [""] * len(current_answers)])
    
    return questions


# Parse the quiz questions
quiz_questions = parse_quiz("quiz.txt")


class Quiz(InstructionsAndUnderstanding):
    def __init__(self, root):
        # Shuffle questions for random order
        shuffled_questions = quiz_questions.copy()
        random.shuffle(shuffled_questions)
        
        super().__init__(
            root,
            controlTexts=shuffled_questions,
            name="Quiz",
            text="Please answer the questions below to the best of your ability.",
            showFeedback=False,
            randomize=True,
            height=3,
            wait=0
        )


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.getcwd()))
    GUI([Quiz])
