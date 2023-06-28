from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(text=q_and_a['text'], answer=q_and_a['answer']) for q_and_a in question_data]

qb = QuizBrain(quiz_list=question_bank)
while qb.still_has_questions():
    qb.next_question()
