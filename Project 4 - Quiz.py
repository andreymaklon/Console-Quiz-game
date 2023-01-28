
import random
from time import sleep
import copy

def play_again():

    while True:
        show = input('Do you want to play again? Y/N: ')
        if show in 'YyNn' and len(show) > 0:
            if show in 'Yy':
                return True
            else:
                return False
        else:
            print('Enter Y or N!')


temp_dictionary = {}
questions = []

# Questions
temp_dictionary['question'] = "Which planet is closest to the Sun?"
temp_dictionary['answera'] = "Mercury"
temp_dictionary['answerb'] = "Venus"
temp_dictionary['answerc'] = "Earth"
temp_dictionary['answerd'] = "Jupiter"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the capital of France?"
temp_dictionary['answera'] = "Paris"
temp_dictionary['answerb'] = "Berlin"
temp_dictionary['answerc'] = "Rome"
temp_dictionary['answerd'] = "London"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the largest planet in our solar system?"
temp_dictionary['answera'] = "Jupiter"
temp_dictionary['answerb'] = "Earth"
temp_dictionary['answerc'] = "Mars"
temp_dictionary['answerd'] = "Saturn"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Which country won the 2018 FIFA World Cup?"
temp_dictionary['answera'] = "France"
temp_dictionary['answerb'] = "Spain"
temp_dictionary['answerc'] = "Germany"
temp_dictionary['answerd'] = "Argentina"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the largest mammal in the world?"
temp_dictionary['answera'] = "Whale"
temp_dictionary['answerb'] = "Elephant"
temp_dictionary['answerc'] = "Giraffe"
temp_dictionary['answerd'] = "Lion"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the name of the process by which plants make food?"
temp_dictionary['answera'] = "Photosynthesis"
temp_dictionary['answerb'] = "Respiration"
temp_dictionary['answerc'] = "Digestion"
temp_dictionary['answerd'] = "Fermentation"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Which element is found in the highest quantity in the Earth's crust?"
temp_dictionary['answera'] = "Oxygen"
temp_dictionary['answerb'] = "Gold"
temp_dictionary['answerc'] = "Silicon"
temp_dictionary['answerd'] = "Carbon"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the name of the longest river in Africa?"
temp_dictionary['answera'] = "Nile"
temp_dictionary['answerb'] = "Congo"
temp_dictionary['answerc'] = "Zambezi"
temp_dictionary['answerd'] = "Niger"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Who invented the telephone?"
temp_dictionary['answera'] = "Alexander Graham Bell"
temp_dictionary['answerb'] = "Thomas Edison"
temp_dictionary['answerc'] = "Nikola Tesla"
temp_dictionary['answerd'] = "Guglielmo Marconi"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the name of the largest desert in the world?"
temp_dictionary['answera'] = "Antarctica"
temp_dictionary['answerb'] = "Sahara"
temp_dictionary['answerc'] = "Atacama"
temp_dictionary['answerd'] = "Gobi"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Which planet in our solar system is known as the 'Red Planet'?"
temp_dictionary['answera'] = "Mars"
temp_dictionary['answerb'] = "Jupiter"
temp_dictionary['answerc'] = "Saturn"
temp_dictionary['answerd'] = "Mercury"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the name of the currency used in Japan?"
temp_dictionary['answera'] = "Yen"
temp_dictionary['answerb'] = "Euro"
temp_dictionary['answerc'] = "Dollar"
temp_dictionary['answerd'] = "Pound"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Which country is the largest producer of coffee in the world?"
temp_dictionary['answera'] = "Brazil"
temp_dictionary['answerb'] = "Colombia"
temp_dictionary['answerc'] = "Ethiopia"
temp_dictionary['answerd'] = "Vietnam"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the name of the highest mountain peak in the world?"
temp_dictionary['answera'] = "Mount Everest"
temp_dictionary['answerb'] = "K2"
temp_dictionary['answerc'] = "Kilimanjaro"
temp_dictionary['answerd'] = "Makalu"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Which element is found in the highest concentration in the human body?"
temp_dictionary['answera'] = "Oxygen"
temp_dictionary['answerb'] = "Carbon"
temp_dictionary['answerc'] = "Hydrogen"
temp_dictionary['answerd'] = 'Nitrogen'

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Which country is known as the land of the rising sun?"
temp_dictionary['answera'] = "Japan"
temp_dictionary['answerb'] = "China"
temp_dictionary['answerc'] = "Korea"
temp_dictionary['answerd'] = "Thailand"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the name of the largest ocean in the world?"
temp_dictionary['answera'] = "Pacific Ocean"
temp_dictionary['answerb'] = "Atlantic Ocean"
temp_dictionary['answerc'] = "Indian Ocean"
temp_dictionary['answerd'] = "Arctic Ocean"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Which planet in our solar system is known as the 'Ice Giant'?"
temp_dictionary['answera'] = "Uranus"
temp_dictionary['answerb'] = "Neptune"
temp_dictionary['answerc'] = "Jupiter"
temp_dictionary['answerd'] = "Saturn"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "Which country is home to the Great Wall of China?"
temp_dictionary['answera'] = "China"
temp_dictionary['answerb'] = "India"
temp_dictionary['answerc'] = "Egypt"
temp_dictionary['answerd'] = "Russia"

questions.append(temp_dictionary.copy())

temp_dictionary['question'] = "What is the capital city of Australia?"
temp_dictionary['answera'] = "Canberra"
temp_dictionary['answerb'] = "Sydney"
temp_dictionary['answerc'] = "Melbourne"
temp_dictionary['answerd'] = "Perth"

questions.append(temp_dictionary.copy())

# Makes a copy of questions to questions_backup, for future use
questions_backup = copy.deepcopy(questions)



# Defines the game function, where the game is
def game():
    global points
    # Counts how many points the player made
    points = 0
    # Counts the current question
    question = 1
    # Shows the question on the screen if it is 0, and then receives 1 to not show it anymore
    i = 0
    # Asks the user if he wants to show correct answers on the screen

    while True:
        show = input('Do you want to show correct answers on the screen if you get it wrong? Y/N: ')
        if show in 'YyNn' and len(show) > 0:
            break
        else:
            print('Enter Y or N!')
    
    while True:
        # If the questions end, the game ends
        if len(questions) == 0:
            break
        # If i is 0, shows the question on the screen, after that, i receives 1
        # Randomly chooses a question from the available questions in the list questions
        if i == 0:
            print()
            chosen_question = random.choice(questions)
            print(f'\033[36mQuestion {question}\033[34m\n{chosen_question["question"]}\033[m')
            question += 1
            i = 1
            del chosen_question['question']
            correct_answer = chosen_question['answera']
            print()
        # Randomly chooses an answer in the list within chosen_question and assigns A, B, C, and D to a different question
        elif len(chosen_question) > 0:
            p = random.choice(list(chosen_question))
            if len(chosen_question) == 4:
                print(f'A: {chosen_question[p]}')
                A = chosen_question[p]
            if len(chosen_question) == 3:
                print(f'B: {chosen_question[p]}')
                B = chosen_question[p]
            if len(chosen_question) == 2:
                print(f'C: {chosen_question[p]}')
                C = chosen_question[p]
            if len(chosen_question) == 1:
                print(f'D: {chosen_question[p]}')
                D = chosen_question[p]

            # Deletes chosen_question[p] after being assigned
            del chosen_question[p]

        else:
            # Exclude an empty dictionary to avoid errors
            questions.remove({})
            while True:
                print()
                # Continues asking the user for their answer until it is A, B, C or D
                while True:
                    answer = input('\033[36mYour answer A/B/C/D: \033[m')
                    if answer in 'AaBbCcDd' and len(answer) > 0:
                        break
                    else:
                        print()
                        print('\033[31mEnter A, B, C, or D!\033[m')

                # Checks if the variable the user chose is the correct answer
                print()
                if answer in 'Aa' and A == correct_answer:
                    print('\033[32mYou got it right! +1 point\033[m')
                    points += 1
                    i = 0
                    sleep(1.5)
                    break

                elif answer in 'Bb' and B == correct_answer:
                    print('\033[32mYou got it right! +1 point\033[m')
                    points += 1
                    i = 0
                    sleep(1.5)
                    break

                elif answer in 'Cc' and C == correct_answer:
                    print('\033[32mYou got it right! +1 point\033[m')
                    points += 1
                    i = 0
                    sleep(1.5)
                    break 

                elif answer in 'Dd' and D == correct_answer:
                    print('\033[32mYou got it right! +1 point\033[m')
                    points += 1
                    i = 0
                    sleep(1.5)
                    break
                
                # If the answer is not correct, the player loses that question and does not receive any points.
                else:
                    print(f'\033[31mYou got it wrong, the correct answer was {correct_answer}\033[m' if show in 'Yy' else f'\033[31mYou got it wrong, and did not earn any points.\033[m')
                    i = 0
                    sleep(1.5)
                    break
while True:
    print()
    # Calls the game function to start the game
    game()
    print()
    print()
    print()
    print(f'\033[32mYou got {points}/20 questions right, for a total of {(points * 100) / 20:.0f}%\033[m')
    print()
    print()
    print()
    # Calls the play_again function and asks the player if they want to play again, if it returns True, the game continues, and if it returns False, the game ends
    pa = play_again()
    if not pa:
        print('See you next time.')
        break
    else:
    # If pa is True, make a copy of questions_backup
        questions = copy.deepcopy(questions_backup)
        