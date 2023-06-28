class QuizBrain:

    def __init__(self, quiz_list):
        self.question_number = 0
        self.question_list = quiz_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        cur_question = self.question_list[self.question_number].text
        cur_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {cur_question}(True/False)?: ")
        if self.check_answer(user_answer, cur_answer):
            self.score += 1
        if self.still_has_questions():
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("")
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_number}")


    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right!")
            return True
        else:
            print("That's wrong")
            print(f"The answer was {current_answer}")
            return False
