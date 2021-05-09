

import question_model
import data
import quiz_brain


question_bank = []

for question in data.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = question_model.Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz Completed.")
print(f"Your Final Score is: {quiz.score}/{quiz.question_number}")


