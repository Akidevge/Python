from quiz_brain import QuizBrain
import tkinter
from tkinter import messagebox
THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.scorecount = 0
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzer APP")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = tkinter.Label(
            text=f"Score: {self.scorecount}", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        self.canvas = tkinter.Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Kanye Quote Goes HERE", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        correctIMG = tkinter.PhotoImage(
            file="day 34\\quizzler-app-start\\images\\true.png")
        wrongIMG = tkinter.PhotoImage(
            file="day 34\\quizzler-app-start\\images\\false.png")
        self.trueBTN = tkinter.Button(
            image=correctIMG, highlightthickness=0, command=self.checkanswertrue)
        self.trueBTN.grid(row=2, column=0)
        self.falseBTN = tkinter.Button(
            image=wrongIMG, highlightthickness=0, command=self.checkanswertrue)
        self.falseBTN.grid(row=2, column=1)
        self.changequestion()
        self.window.mainloop()

    def changequestion(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            messagebox.showinfo(title="Game over",
                                message=f"Final score: {self.scorecount}")

    def checkanswertrue(self):
        ans = self.quiz.checkforans()
        if ans == "True":
            self.scorecount += 1
            self.givefeedback(feedback=True)
        else:
            self.givefeedback(feedback=False)
        self.updatescore()
        self.changequestion()

    def checkanswerfalse(self):
        ans = self.quiz.checkforans()
        if ans == "False":
            self.scorecount += 1
            self.givefeedback(feedback=True)
        else:
            self.givefeedback(feedback=False)
        self.updatescore()
        self.changequestion()

    def updatescore(self):
        self.score.config(text=f"Score: {self.scorecount}")

    def givefeedback(self, feedback):
        if feedback:
            messagebox.showinfo(title="Hurray!",
                                message="Correct Answer")
        else:
            messagebox.showinfo(title="Ooops!",
                                message="Wrong Answer")
