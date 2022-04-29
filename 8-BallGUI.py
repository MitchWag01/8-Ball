import random as r
from tkinter import *

# create basic function for 8-ball.
def eight_ball():
    """
    Purpose: To calculate the output of the eightball and to update the text displayed.
    Post-Condition: label text will be updated to appropriate output.
    Return: None
    """
    # get input from text box.
    question_input = question_txt_box.get(1.0, "end-1c")
    # account for an empty box and short text.
    if question_input == "":
        text.set("This can't be blank.")
    elif len(question_input) < 8:
        text.set("Please ask a longer question :)")
    else:
        # find a random int and assign output text for all options.
        random_number = r.randint(1, 9)
        adict = {1: "Definitely", 2: "Decidedly so", 3: "Without a doubt.", 4: "Reply hazy, try again.",
             5: "Ask again later.", 6: "Better not tell you now.", 7: "My sources say no.", 8: "Outlook not so good.",
             9: "Very doubtful."}

        # iterate through the dictionary, print the result to both console and application.
        for num, val in enumerate(adict.values()):
            if random_number == num:
                print(f'You asked: {question_input}?')
                print(f"Magic 8-Ball's answer: {val}")
                text.set(f"Magic 8-Ball's answer: {val}")


# create starting frame, label and assign text.
frame = Tk()
frame.title("8-Ball-Fortune-Teller")
frame_label = Label(frame, text="Ask a yes or no question")
frame_label.pack()
frame.geometry('600x300')

# create textbox to enter question.
question_txt_box = Text(frame, height=1, width=50)
question_txt_box.pack()

# create starting text.
text = StringVar()
text.set("Ask a Question!")

# create answer text.
answer_label = Label(frame, textvariable=text)
answer_label.pack()

# create button to update text.
enter_button = Button(frame, text="Ask!", command=eight_ball)
enter_button.pack()

frame.mainloop()
