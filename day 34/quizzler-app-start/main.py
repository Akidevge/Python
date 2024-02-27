from question_model import Question
from quiz_brain import QuizBrain
from ui import UI
import requests
import json
# request=requests.get("https://opentdb.com/api.php?amount=10&category=15&type=boolean")
# QuizBank=request.json()["results"]
# with open("day 34\\quizzler-app-start\\data.py","w") as File:
#     File.write("QuestionList=")
#     File.write(json.dumps(QuizBank))
question_bank = []
from data import QuestionList
for question in QuestionList:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
userInterface=UI(quiz)
while quiz.still_has_questions():
    quiz.next_question()


# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
