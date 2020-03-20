import random

def init():
    global problem_text
    global correct_guesses
    global incorrect_guesses
    global guess_count
    global guess_char

    file = '/Users/bharadwaj/PycharmProjects/HelloPy/hangman_project/input.txt'
    with open(file) as f:
        content = f.read().splitlines()
    problem_text = random.choice(content)

    correct_guesses = []
    incorrect_guesses = []
    guess_count = 5
    guess_char = ''
