import random

print("Welcome To The Game!\n")
print("I am thinking of a number between 1 and 100\n")

difficulty = input('Choose a difficulty level: "easy" or "hard"\n')

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate_random_number():
    rand = random.randint(0, 9)
    return rand

def generate_number():
    random_number = 0
    number_of_places = random.randint(1, 3)
     
    if number_of_places == 1:
        random_number_position = generate_random_number()
        random_number = numbers[random_number_position]
    elif number_of_places == 2:
        random_number_position1 = generate_random_number()
        random_number_position2 = generate_random_number()
        random_number = str(numbers[random_number_position1]) + \
            str(numbers[random_number_position2])
    elif random_number == 3:
        random_number = 100

    return random_number


def game_board():
    guess = int(input("Make a guess:  "))


def attempts_counter(difficulty):
    if difficulty == "easy":
        print("You have 10 attempts top guess this number")
    else:
        print("You have 5 attempts top guess this number")


if difficulty == "easy":
    attempts_counter(difficulty)
else:
    attempts_counter(difficulty)
