from tkinter import *
import html

class QuizInterface:

    def __init__(self, quizbrain):
        self.quizbrain = quizbrain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx = 15,
                           pady = 15,
                           bg = "gray")

        self.canvas2 = Canvas(width = 500,
                              height = 500,
                              bg = 'steelblue3')
        self.canvas2.grid(row = 0, column = 0, columnspan= 2)

        self.canvas1 = Canvas(width = 400,
                             height = 400,
                             bg="cadetblue1",
                             highlightthickness=0)
        self.canvas1.grid(row = 0, column=0, columnspan=2)


        #texts on canvas
        self.score_text = self.canvas2.create_text(250, 25, text = "SCORE: 0",font = ("Comic Sans Ms", 15, 'normal'))

        self.question_number_text = self.canvas1.create_text(200, 40,
                                                             text="Question no.",
                                                             font=("Courier", 20, "normal"))

        self.question_text = self.canvas1.create_text(200,
                                                     225,
                                                     text="Question",
                                                     font = ("Courier", 15, "bold"),

                                                     width = 350)

        #images
        correct_img = PhotoImage(file = "./images/true.png")
        wrong_img = PhotoImage(file = "./images/false.png")


        #buttons
        self.true_b = Button(image = correct_img, command = self.true_pressed, highlightthickness = 0)
        self.true_b.grid(row = 1, column = 0, pady = 10)

        self.false_b = Button(image = wrong_img,command = self.false_pressed, highlightthickness = 0)
        self.false_b.grid(row=1, column=1, pady = 10)


        self.next_question()

        self.window.mainloop()

    # this will retrive the next question from the quizbrain and display it
    def next_question(self):
        self.canvas1.configure(bg = "cornsilk")
        if self.quizbrain.still_got_questions():
            question_info = self.quizbrain.next_question()
            question_text = html.unescape(question_info[0])
            question_number = question_info[1]
            self.canvas1.itemconfig(self.question_text, text = f"'{question_text}'", font = ("Arial", 19, "bold"))
            self.canvas1.itemconfig(self.question_number_text, text = f"Question{question_number+1}:", font=("Courier", 23, "bold"))
        else:
            self.canvas1.itemconfig(self.question_text, text = "Quiz is over!!!"
                                                               f"\nYou have answered {self.quizbrain.score} questions out "
                                                               f"of {len(self.quizbrain.q_list)} questions correctly.")

            self.disable_butons()

    def true_pressed(self):
        if self.quizbrain.check_answer(user_input="True"):
            self.canvas1.configure(bg="green")
            self.window.after(1000, self.next_question)
            self.quizbrain.score += 1
            self.canvas2.itemconfig(self.score_text, text = f"SCORE: {self.quizbrain.score}",
                                   font = ("Comic Sans Ms", 15, 'normal'))
        else:
            self.canvas1.configure(bg="red")
            self.window.after(1000, self.next_question)


    def false_pressed(self):
        if self.quizbrain.check_answer(user_input = "False"):
            self.canvas1.configure(bg = "green")
            self.window.after(1000, self.next_question)
            self.quizbrain.score += 1
            self.canvas2.itemconfig(self.score_text, text=f"SCORE: {self.quizbrain.score}",
                                   font=("Comic Sans Ms", 15, 'normal'))

        else:
            self.canvas1.configure(bg="red")
            self.window.after(1000, self.next_question)

    def disable_butons(self):
        self.true_b.config(state = DISABLED)
        self.false_b.config(state= DISABLED)

