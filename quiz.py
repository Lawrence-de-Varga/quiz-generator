from menus import *
from random import choice
import pprint as pp

example_answer_key = {"What is the capital of Victoria?" : "Melbourne",
                     "What is the capital of New South Wales?" : "Sydney",
                     "What is the capital of Queensland?" : "Brisbane",
                     "What is the capital of the Northern Territory?" : "Darwin",
                     "What is the capital of Western Australia?" : "Perth",
                     "What is the capital of South Australia?" : "Adelaide",
                     "What is the capital of Tasmania?" : "Hobart",
                     "What is the capital of the Australian Capital Territory?" : "Canberra"}

ex_quiz = {}

def random_answers_list(answer_key, question, answers, num_of_ans):
    answers_list = [answer_key[question]]
    answers = [answer for answer in answers if answer != answer_key[question]]

    for num in range(1, 1 + num_of_ans):
        new_answer = choice(answers)
        answers_list.append(new_answer)
        answers = [answer for answer in answers if answer != new_answer]

    return sorted(answers_list)

def random_questions_list(questions, num_of_questions):
    questions_list = list(questions)
    new_questions_list = []

    for num in range(1, 1 + num_of_questions):
        a_question = choice(questions_list)
        new_questions_list.append(a_question)
        questions_list = [question for question in questions_list if question != a_question]

    return new_questions_list

def get_topic():
    return prompt("What is the topic of the quiz?")

def get_question():
    return prompt("Please enter a question.")

def get_answer():
    return prompt("Please enter an answer.")

def create_answer_key(quiz):
    num_of_questions = get_nn_int(message = "How many questions should the quiz have? (Enter 0 to exit)")

    if num_of_questions == 0:
        return
    else:
        for num in range(1, num_of_questions + 1):
            question = get_question()
            quiz[question] = get_answer()

def create_quiz(answer_key):
    possible_questions = answer_key.keys()
    possible_answers = answer_key.values()
    num_of_pos_questions = len(possible_questions)

    new_quiz = {}

    inp_type = f"number between 0 and {num_of_pos_questions}"
    func = lambda x: x >= 0 and x <= num_of_pos_questions
    num_of_questions = get_int("How many questions should the quiz have? (Enter 0 to quit)",
                               inp_type, func)

    if num_of_questions == 0:
        return
    
    num_of_answers = get_int("How many possible answers should each question have? (Enter 0 to exit)",
                             inp_type, func)
    if num_of_answers == 0:
        return

    questions = random_questions_list(possible_questions, num_of_questions)
    
    for question in questions:
        new_quiz[question] = random_answers_list(answer_key, question, possible_answers, num_of_answers)

    return new_quiz

    

def modify_quiz():
    pass

def delete_quiz():
    pass



def menu():

    menu_options = ['Create a new Quiz', 'Modify an existing Quiz', 'Delete a Quiz']

    options = print_options(gen_options(menu_options, 'action', 'take', every=False))
    
    for index, options in options.items():
        options[index] = first_word(option)


    action = select_options(options, 'action', 'take')[0]

    if action == 'create':
        create_quiz()
    elif action == 'modify':
        modify_quiz()
    elif action == 'delete':
        delete_quiz()
    elif action == 'exit':
        print("Goodbye.")
    else:
        bad_option(action)

a = create_quiz(example_answer_key)
pp.pprint(a)

#create_answer_key(ex_quiz)

#print(ex_quiz)











