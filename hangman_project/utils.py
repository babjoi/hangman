import os
import time
from hangman_project import settings


def display_result(correct_guesses):
    display_text = settings.problem_text
    for each_char in display_text:
        if each_char.lower() not in correct_guesses:
            display_text = display_text.replace(each_char, "_ ")
    return display_text


def display_hangman(guess_count):
    hangman_file = '/Users/bharadwaj/PycharmProjects/HelloPy/hangman_project/hangman_image'
    if guess_count != 0:
        with open(hangman_file) as f_stream:
            for count in range(1, (5 - (guess_count - 1))):
                print(f_stream.readline().strip())
    else:
        with open(hangman_file) as f_stream:
            for blink_count in range(1, 5):
                time.sleep(0.2)
                os.system("clear")
                time.sleep(0.3)
                f_stream.seek(0, 0)
                for i in range(1, 5):
                    print(f_stream.readline().strip())
            os.system("clear")
            f_stream.seek(0, 0)
            for count in range(1, 6):
                f_stream.readline().strip()
            for count in range(1, 6):
                print(f_stream.readline().rstrip())
