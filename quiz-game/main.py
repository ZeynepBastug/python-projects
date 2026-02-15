from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for i in question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)


quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")