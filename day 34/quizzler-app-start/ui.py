THEME_COLOR = "#375362"
import tkinter
from quiz_brain import QuizBrain
class UI:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzer APP")
        self.window.config(padx=20, pady=20,background=THEME_COLOR)
        self.score=tkinter.Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0, column=1)
        self.canvas = tkinter.Canvas(width=300, height=250,background="white")
        self.question_text =self.canvas.create_text(150,125,text="Kanye Quote Goes HERE",fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)
        self.correctIMG=tkinter.PhotoImage(file="day 34\\quizzler-app-start\\images\\true.png")
        self.wrongIMG=tkinter.PhotoImage(file="day 34\\quizzler-app-start\\images\\false.png")
        self.trueBTN=tkinter.Button(image=self.correctIMG,highlightthickness=0)
        self.trueBTN.grid(row=2, column=0)
        self.falseBTN=tkinter.Button(image=self.wrongIMG,highlightthickness=0)
        self.falseBTN.grid(row=2, column=1)
        self.window.mainloop()
    def changequestion(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)

