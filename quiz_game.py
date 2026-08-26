import random

questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Program Utility", "D. Core Processing Unit"],
        "answer": "A"
    },
    {
        "question": "Which language is known as the language of the web?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A. Read Access Memory", "B. Random Access Memory", "C. Run Access Memory", "D. Random Array Memory"],
        "answer": "B"
    },
    {
        "question": "Which of these is a version control system?",
        "options": ["A. Python", "B. GitHub", "C. Git", "D. JSON"],
        "answer": "C"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    }
]

def run_quiz():
    print("=== Tech Quiz Game ===")
    score = 0
    random.shuffle(questions)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").upper()
        
        if answer == q['answer']:
            print("Correct! ✓")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}")
    
    print(f"\n=== Quiz Complete ===")
    print(f"You scored {score}/{len(questions)}")
    
    if score == len(questions):
        print("Perfect score!")
    elif score >= 3:
        print("Good job!")
    else:
        print("Keep practising!")

def main():
    while True:
        run_quiz()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

main()
