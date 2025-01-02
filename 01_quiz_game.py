questions = [
    {
        "question": "The Earth is flat.",
        "options": ["False", "True"],
        "answer": "False"
    },
    {
        "question": "Python is a type of snake.",
        "options": ["False", "True"],
        "answer": "True"
    },
    {
        "question": "The capital of France is Berlin.",
        "options": ["False", "True"],
        "answer": "False"
    },
    {
        "question": "Water boils at 100 degrees Celsius.",
        "options": ["False", "True"],
        "answer": "True"
    },
    {
        "question": "Humans can breathe underwater without any equipment.",
        "options": ["False", "True"],
        "answer": "False"
    },
]

score = 0
count = 1

print("Let's Start Your Quiz Game, Answer by pressing 0 = False, 1 = True")

for question in questions:
    while True: 
        print(f"\n{count}. {question['question']}")
        ans = input("Enter your choice, 0 = False 1 = True: ")
        if ans !='0' and ans !='1':
            print("Invalid !, Try Again!")
            continue
        elif(ans == '0' and question['answer'] == 'False'):
            print("Correct Answer")
            score += 1
        elif(ans == '1' and question['answer'] == 'True'):
            print("Correct Answer")
            score += 1
        else:
            print("Incorrect Answer!")
        count += 1
        break

print(f"\nYour Final score is {score}/{count-1}")