import random

print("Welcome To The Game!\n")
print("I am thinking of a number between 1 and 100\n")

difficulty = input('Choose a difficulty level: "easy" or "hard"\n')
attempts = 0

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
    elif number_of_places == 3:
        random_number = 100

    return random_number


def game_board(attempts):
    random_number = generate_number()
    _attempts = attempts

    while _attempts > 0:
        guess = int(input("Make a guess:  "))
        if guess > int(random_number):
            print("Too high\n")
            _attempts -= 1
            print(f"You have {_attempts} attempts\n")

        elif guess < int(random_number):
            print("Too low")
            _attempts -= 1
            print(f"You have {_attempts} attempts\n")
        elif guess == int(random_number):
            return print("Correct you won")

    if _attempts == 0:
        return print("You Lost Stupid Ass")


if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts to guess this number")
    game_board(10)
elif difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} attempts to guess this number")
    game_board(5)
