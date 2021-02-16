from Question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = [Question(question['text'], question['answer'], question['options']) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    if not quiz.still_has_questions():
        print(f"You've completed the quiz, and your score is {quiz.score}/{len(quiz.question_list)}")

