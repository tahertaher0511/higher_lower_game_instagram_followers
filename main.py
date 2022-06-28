from art import logo, vs
import random
from game_data import data
from os import system, name


def clear():
    """This function will clear the screen to start over new game. Then whenever you want to clear the screen,
    just use this clear function Then go for main.py and modify the  configuration to and checks the box if imulate
    terminal in output console is activate.
    """
    if name == "nt":  # for windows the name is 'nt'
        _ = system("cls")
    else:
        # and for mac and linux, the os.name is "posix"
        _ = system("clear")


print(logo)
play_game = True
score = 0
count_a = random.choice(data)
count_b = random.choice(data)

while play_game:
    def count_info(count):
        """Takes account information and return it as formatted account info."""
        name_count = count["name"]
        description_count = count["description"]
        country_count = count["country"]
        return f"{name_count}, A {description_count}, From {country_count}."


    def check_answer(user_guess, follower_a, follower_b):
        """Take the user guess and followers counts if they got it right."""
        if follower_a > follower_b:
            return user_guess == "a"
        else:
            return user_guess == "b"


    follower_count_a = count_a["follower_count"]
    follower_count_b = count_b["follower_count"]

    if follower_count_a == follower_count_b:
        count_b = random.choice(data)

    print(f"Compare A: {count_info(count_a)}")
    print(vs)
    print(f"Against B: {count_info(count_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = check_answer(guess, follower_count_a, follower_count_b)
    clear()
    print()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

        if follower_count_a > follower_count_b:
            count_a = count_a
            count_b = random.choice(data)
        else:
            count_a = count_b
            count_b = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game = False
