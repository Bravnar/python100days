from tkinter import *
from quiz_brain import QuizBrain


FONT = ("Arial", 20, "italic")
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="",
            font=FONT,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_img = PhotoImage(file="images/true.png")
        self.button_true = Button(
            image=true_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.answer_true
        )
        false_img = PhotoImage(file="images/false.png")
        self.button_false = Button(
            image=false_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.answer_false
        )
        self.button_true.grid(row=2, column=0, padx=49)
        self.button_false.grid(row=2, column=1, padx=49)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
        
    
    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    
    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right: self.canvas.config(bg="green")
        else: self.canvas.config(bg="red")
        delay = self.window.after(1000, self.get_next_question)