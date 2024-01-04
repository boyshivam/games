from data import QuestionList
from Question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


questions_set = []
questions_list =  QuestionList()
list_of_q = questions_list.questions


for q in list_of_q:
    q_text = q['question']
    q_answer = q['correct_answer']
    question = Question(q_text, q_answer)
    questions_set.append(question)

quizbrain = QuizBrain(questions_set)
quizui = QuizInterface(quizbrain)






