# Python quiz game

questions= ("What is 9+10?",
            "Why did the chicken cross the road?",
            "Who do I main?")

options = (("A. 19", "B. 21", "C. 910", "D. I don't do math"),
           ("A. To get to the other side", "B. Because it saw a KFC", "C. It was chasing a worm", "D. It lost a bet"),
           ("A. Jett", "B. Sage", "C. Omen", "D. Phoenix"))

answers = ("B", "A", "C")
guesses = []

score = 0
question_num = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    print()
    guess = input("Enter an answer: ").upper()
    guesses.append(guess)
    print()
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"The correct answer was {answers[question_num]}")
    question_num += 1
    
print("----------------")
score = float(score / len(questions) * 100) 
print(f"Your score is {score:.02f}%")

print("Answers: ", end="")
for answer in answers:
    print(answer, end = " ")
print()
    
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end = " ")
print()