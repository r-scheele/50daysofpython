
class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def still_has_questions(self):
        """Checks if question is left"""
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        """Returns True if correct answer was chosen, otherwise False"""
        return answer == correct_answer

    def next_question(self):
        """Returns the next question in the question list."""

        question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {question.text}")

        print(f"A. {question.options['a']}  B. {question.options['b']} C. {question.options['c']}")
        if self.check_answer(question.answer.lower(), question.options[input().lower()].lower()):
            self.score += 1
        return


