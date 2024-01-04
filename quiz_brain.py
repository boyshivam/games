import html


class QuizBrain:

    def __init__(self, q_list):
        self.q_list = q_list
        self.score = 0
        self.question_number = 0

    def still_got_questions(self):
        return self.question_number < len(self.q_list)

    def next_question(self):
        self.current_question = self.q_list[self.question_number]
        self.c_question_number = self.question_number
        self.question_number += 1
        return self.current_question.q_text, self.c_question_number

    def check_answer(self, user_input):
        self.correct_answer = self.current_question.q_answer
        if user_input == self.correct_answer:
            return True
        else:
            return False
