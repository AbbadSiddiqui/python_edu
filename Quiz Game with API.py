import requests
import random
import html

#questions = ("How many elements are in the periodic table?: ",
#                       "Which animal lays the largest eggs?: ",
#                       "What is the most abundant gas in Earth's atmosphere?: ",
#                       "How many bones are in the human body?: ",
#                       "Which planet in the solar system is the hottest?: ")
#options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#                   ("A. 206", "B. 207", "C. 208", "D. 209"),
#                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
#answers = ("C", "D", "A", "A", "B")

def fetch_questions():
    url = "https://opentdb.com/api.php?amount=10&type=multiple"
    response = requests.get(url)
    data = response.json()
    questions_data = data['results']
    
    questions = []
    options = []
    answers = []
    correct_letters = []  # New list to store correct letter answers

    for item in questions_data:
        question = html.unescape(item['question'])
        correct_answer = html.unescape(item['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in item['incorrect_answers']]
        
        all_answers = incorrect_answers + [correct_answer]
        random.shuffle(all_answers)
        
        # Store the letter (A, B, C, D) of the correct answer
        correct_letter = chr(65 + all_answers.index(correct_answer))
        
        questions.append(question)
        options.append(all_answers)
        answers.append(correct_letter)  # Store letter instead of full answer

    return questions, options, answers

def quiz_game():
    questions, options, answers = fetch_questions()
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for i, option in enumerate(options[question_num]):
            print(f"{chr(65 + i)}. {option}")

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        
        if guess == answers[question_num]:  # Compare letters directly
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
    for answer in answers:  # Will now print letters (A, B, C, D)
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()
    print(f"Your score is: {score}/{len(questions)}")

# Run the quiz game
quiz_game()