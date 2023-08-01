THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
import time

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        #Canvas 
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        # Question 
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="BlahBlahBlah",
            font=("Arial", 20, "italic"), fill=THEME_COLOR)
        
        #Score
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)
        
        
        
        # Button
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.press_true_btn)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.press_false_btn)
        self.false_btn.grid(row=2, column=1)
        
        self.get_next_question()
        
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions() is True:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.configure(bg="white")
        else:
            self.canvas.itemconfig(self.question_text,text="End")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def press_true_btn(self):
        user_answer = "True"
        is_right = self.quiz.check_answer(user_answer=user_answer)
        self.give_feedback(is_right)
        
    def press_false_btn(self):
        user_answer = "False"
        is_right = self.quiz.check_answer(user_answer=user_answer)
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")            
        self.window.after(1000, self.get_next_question)                  
        self.score_label.config(text=f"Score: {self.quiz.score}")
