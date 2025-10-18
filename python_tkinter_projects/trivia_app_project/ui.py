from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
QUESTION_TEXT_FONT = ("Arial",20,"italic")


class TriviaInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain

        self.window.title("Trivia Game")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        right_photo = PhotoImage(file="images/true.png")
        wrong_photo = PhotoImage(file="images/false.png")

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(150,125,
                                                     text="Question here",
                                                     font=QUESTION_TEXT_FONT,
                                                     fill = THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)

        self.right_button = Button(image=right_photo, highlightthickness=0, command=self.button_true)
        self.right_button.grid(row=2,column=0)

        self.wrong_button = Button(image=wrong_photo, highlightthickness=0, command=self.button_false)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.activated_buttons()
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the trivia.\n"
                                                            f"Your final score is\n {self.quiz.score} / 10")
            self.disabled_buttons()

    def disabled_buttons(self):
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

    def activated_buttons(self):
        self.right_button.config(state="active")
        self.wrong_button.config(state="active")

    def button_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def button_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.disabled_buttons()
        self.window.after(1000, func=self.get_next_question)

