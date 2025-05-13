questions = ("What is the correct file extension for Python files?: ",
             "Which keyword is used to create a function in Python?: ",
             "What will `print(2 ** 3)` output?: ",
             "Which data type is used to store True or False values?: ",
             "What is the output of: `len([1, 2, 3, 4])`?: ")

             


options = (("A. .pyth", "B. .pt", "C. .py", "D. .pyt"),
           ("A. define", "B. function", "C. def", "D. fun"),
           ("A. 6", "B. 8", "C. 9", "D. 5"),
           ("A. int", "B. bool", "C. str", "D. float"),
           ("A. 3", "B. 4", "C. 5", "D. Error"))

answers = ("C", "C", "B", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")