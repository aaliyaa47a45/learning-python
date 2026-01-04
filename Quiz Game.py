print("Welcome to the Python Quiz Game")
print("-----------------------------------")

questions=[
    {
        "question":"What is the capital of India?",
        "options":["A.Mumbai","B.Delhi","C.Kolkata","D.Chennai"],
        "answer":"B"
    },
    {
        "question":"Which language is used for AI?",
        "options":["A.Python","B.HTML","C.CSS","D.SQL"],
        "answer":"A"
    },
    {
        "question":"What is 5+7?",
        "options":["A.10","B.11","C.12","D.13"],
        "answer":"C"
    },
    {
        "question":"Who developed Python?",
        "options":["A.Elon Musk","B.Bill Gates","C.Cuido van Rossum","D.Mark Zuckerberg"],
        "answer":"C"
    },
    ]

score=0

for q in questions:
        print("\n" + q["question"])
for option in q["options"]:
        print(option)
user_answer=input("Enter your answer(A/B/C/D):").upper()
if user_answer==q["answer"]:
        print("Correct!")
        score+=1
else:
        print("Wrong!")


print("\n Quiz Completed")
print("Your Score:",score,"/",len(questions))

