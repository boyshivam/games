# this class handles the mechanics of the game
class QuizBrain:

    def __init__(self, q_list):
        self.q_list = q_list
        self.score = 0
        self.question_number = 0

    # it checks for availability of questions in a list
    def still_got_questions(self):
        return self.question_number < len(self.q_list)

    # it gets the next question in list
    def next_question(self):
        self.current_question = self.q_list[self.question_number]
        self.c_question_number = self.question_number
        self.question_number += 1
        return self.current_question.q_text, self.c_question_number

    # it compares the user input with the actual answer
    def check_answer(self, user_input):
        self.correct_answer = self.current_question.q_answer
        if user_input == self.correct_answer:
            return True
        else:
            return False
