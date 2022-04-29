import random as r

name = "Mitchell"
question = input('enter a question: ')
answer = ""
random_number = r.randint(1, 9)
adict = {1: "definitely", 2: "decidedly so", 3: "Without a doubt.", 4: "Reply hazy, try again.", 5: "Ask again later.",
         6: "Better not tell you now.", 7: "My sources say no.", 8: "Outlook not so good.", 9: "Very doubtful."}
for num, val in enumerate(adict.values()):
  if random_number == num:
    print(f'{name} asks: {question}?')
    print(f"Magic 8-Ball's answer: {val}")
