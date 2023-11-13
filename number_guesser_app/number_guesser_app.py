import random

def the_game(low_range, high_range):
    count = 5
    correct_answer = random.randint(low, high)
    print(correct_answer)

    print('--------------------------------------------')
    print(f'Guess a number between {low_range} and {high_range}')
    print('--------------------------------------------')

    while True:
        if count != 5:
            print(' - - - - - - - - - ')

        print(f'{count} chances left!')
        user_input = input('Enter your guess: ')

        if user_input.isdigit():
            user_input = int(user_input)
        else:
            count -= 1
            if count == 0:
                print('\n>>>>>>> You Lose! <<<<<<<')
                break
            continue

        if user_input == correct_answer:
            print('\n>>>>>>> You Win! <<<<<<<')
            break
        elif user_input < correct_answer and count > 1:
            print('Hint: The number is bigger')
        elif user_input > correct_answer and count > 1:
            print('Hint: The number is smaller')

        count -= 1
        if count == 0:
            print('\n>>>>>>> You Lose! <<<<<<<')
            break



low = 1
high = 10

the_game(low, high)

while True:

    choice = input('\nWant to try again? Y/N : ').lower()

    if choice == 'y':
        the_game(low, high)
    else:
        break