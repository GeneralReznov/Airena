import os
import random
from fluvio import Fluvio

# Folder where your genre text files are stored
QUESTIONS_DIR = r"D:\Sumukhi Files\Stuff\hackahazards\Questions"

def list_available_genres():
    files = os.listdir(QUESTIONS_DIR)
    genres = [os.path.splitext(f)[0].lower() for f in files if f.endswith(".txt")]
    return genres

def load_questions_from_file(genre):
    path = os.path.join(QUESTIONS_DIR, f"{genre}.txt")
    if not os.path.isfile(path):
        return []
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        questions = []
        for line in lines:
            if '|' in line:
                q, a, *options = line.strip().split('|')
                questions.append({'q': q.strip(), 'a': a.strip(), 'options': options})
        return questions

def get_random_questions(questions, count=3):
    return random.sample(questions, min(count, len(questions)))

def run_quiz():
    genres = list_available_genres()

    if not genres:
        print("No genres found. Please add genre .txt files in the 'questions' folder.")
        return

    print("Available Genres:")
    for g in genres:
        print(f" - {g.title()}")

    genre = input("\nEnter your preferred genre: ").strip().lower()

    if genre not in genres:
        print("Invalid genre selected.")
        return

    questions = load_questions_from_file(genre)
    if not questions:
        print(f"No questions found for genre: {genre}")
        return

    # Fluvio event producer and consumer
    fluvio = Fluvio.connect()
    producer = fluvio.topic_producer("quiz-events")
    producer.send_string(f"[QUIZ] Genre selected: {genre}")

    selected_questions = get_random_questions(questions, 5)
    score = 0

    print(f"\nStarting Quiz in '{genre.title()}' Genre:")
    for i, q in enumerate(selected_questions, 1):
        print(f"\nQ{i}: {q['q']}")
        options = q['options'] + [q['a']]
        random.shuffle(options)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        try:
            answer_index = int(input("Your answer (1/2/3/4): ").strip()) - 1
            if options[answer_index].lower() == q['a'].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. Correct answer: {q['a']}")
        except (ValueError, IndexError):
            print(f"Invalid input. Correct answer: {q['a']}")

    result_msg = f"[QUIZ RESULT] Genre: {genre}, Score: {score}/{len(selected_questions)}"
    print("\n" + result_msg)
    producer.send_string(result_msg)

if __name__ == "__main__":
    run_quiz()

