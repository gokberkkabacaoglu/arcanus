""" 
    quiz.py
"""

from Tkinter import *
from tkMessageBox import *

class Problem(object):
  def __init__(self, question = "", a = "", b = "", c = "", correct = ""):
    object.__init__(self)
    self.question = question
    self.a = a
    self.b = b
    self.c = c
    self.correct = correct
    
class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    self.problems = []
    self.counter = 0

    self.addComponents()
    
  def addComponents(self):
    """ add components to the GUI """

    self.title("Quiz")
    #force app to a fixed width
    self.grid()
    self.columnconfigure(0, minsize = 100)
    self.columnconfigure(1, minsize = 200)
    self.columnconfigure(2, minsize = 100)

    self.lblQuestion = Label(self, text = "Question")
    self.lblQuestion.grid(columnspan = 3, sticky = "we")
    
    # self.btnA = Button(self, text = "A", command = self.checkA)
    # self.btnA.grid(columnspan = 3, sticky = "we")
    
    # self.btnB = Button(self, text = "B", command = self.checkB)
    # self.btnB.grid(columnspan = 3, sticky = "we")
    
    # self.btnC = Button(self, text = "C", command = self.checkC)
    # self.btnC.grid(columnspan = 3, sticky = "we")
    
    self.btnPrev = Button(self, text = "prev", command = self.prev)
    self.btnPrev.grid(row = 4, column = 0)
    
    self.lblCounter = Label(self, text = "0")
    self.lblCounter.grid(row = 4, column = 1)
    
    self.btnNext = Button(self, text = "next", command = self.next)
    self.btnNext.grid(row = 4, column = 2)

  def run(self):
    self.showProblem(0)
    self.mainloop()
      
  def checkA(self):
    self.check("A")

  def checkB(self):
    self.check("B")

  def checkC(self):
    self.check("C")
    
  def check(self, guess):
    #compares the guess to the correct answer
    correct = self.problems[self.counter].correct
    if guess == correct:
      showinfo("Quiz", "Correct")
    else:
      showinfo("Quiz", "Wrong!")
      
  def prev(self):
    self.counter -= 1
    if self.counter < 0:
      self.counter = 0
    self.showProblem(self.counter)
    
  def next(self):
    self.counter += 1
    if self.counter >= len(self.problems):
      self.counter = len(self.problems) - 1
    self.showProblem(self.counter)

  def showProblem(self, counter):
    self.lblQuestion["text"] = self.problems[counter].question
    #self.btnA["text"] = self.problems[counter].a
    #self.btnB["text"] = self.problems[counter].b
    #self.btnC["text"] = self.problems[counter].c
    self.lblCounter["text"] = self.counter

  def loadProblems(self):

    # If you can read this, you have gone too far
    self.problems.append(Problem(
      "What is the airspeed velocity of an unladen swallow?",
      "African or European?",
      "5.8 meters per second",
      "2 mph",
      "A"))    
