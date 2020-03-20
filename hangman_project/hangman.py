import os
import time

import hangman_project.utils as utils
import hangman_project.settings as settings
# from hangman_project import utils, settings


def f_append_guessed_char(correct, incorrect):
    if correct.isalpha():
        settings.correct_guesses.append(correct)
    if incorrect.isalpha():
        settings.incorrect_guesses.append(incorrect)


def f_update_guess_count():
    settings.guess_count -= 1


def f_check_completion():
    count = 0
    for each_char in settings.problem_text:
        if each_char.lower() not in settings.correct_guesses:
            count += 1
    if count == 0:
        os.system("clear")
        print(f"\n {utils.display_result(settings.correct_guesses).upper()} \n")
        print(f"You go it with {settings.guess_count} tries left! \n")
        exit(0)
    else:
        f_guess_the_char()


def f_validate_char(guess_char):
    if settings.guess_count == 0:
        should_play_again = input("Game Over. Try again? (y/n): ").lower()
        if should_play_again == 'y':
            settings.init()
            f_guess_the_char()
        else:
            exit(0)
    elif guess_char in list(settings.correct_guesses + settings.incorrect_guesses):
        print(f"{guess_char.upper()} - Guessed it already")
        time.sleep(0.5)
        f_guess_the_char()
    elif guess_char in settings.problem_text:
        f_append_guessed_char(correct=guess_char, incorrect="")
        f_check_completion()
    else:
        f_update_guess_count()
        f_append_guessed_char(correct="", incorrect=guess_char)
        print(f"Wrong Guess!! {settings.guess_count} guesses left")
        f_guess_the_char()


def f_guess_the_char():
    os.system("clear")
    print(utils.display_result(settings.correct_guesses).upper())
    utils.display_hangman(settings.guess_count)
    if settings.guess_count != 0 :
        if len(settings.incorrect_guesses) != 0:
            print(f"Incorrect guesses: {settings.incorrect_guesses}")
        settings.guess_char = input(f"Guess the {len(settings.problem_text)} letter word in {settings.guess_count} guesses: ")
    f_validate_char(settings.guess_char)


settings.init()
f_guess_the_char()
