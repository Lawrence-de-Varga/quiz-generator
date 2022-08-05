def prompt(message):
    """ Used to prompt the user to input"""
    print(message)
    return input(">> ")

def bad_option(option):
    print(f"Sorry '{option}' is not a valid option.")

def bad_input(inp, input_type):
    print(f"Sorry, '{inp}' is not a valid {input_type}.")

def get_int(message = "PLease enter a integer.", input_type = "integer", test = lambda x: int(x)):
    inp = prompt(f"{message}")

    try:
        inp = int(inp)
    except ValueError:
        bad_input(inp, input_type)
        return get_int()

    if not test(inp):
        bad_input(inp, input_type)
        return get_int()
    else: 
        return inp

def get_nn_int(message="Please enter a non negative integer.", 
               input_type = "non negative integer",
               text = lambda x: x >= 0):
        return get_int(message, input_type, text)

############################################ Menu Presentation and Selection #################################
# NOTE articles_and_others is not necessarily complete  
articles_and_others = ['the', 'a', 'an', 'and', 'on', 'in', 'of', 'some', 'from']
 
def format_name(name):
    """ Takes a name and capitalizes every word not in articules_and_others. E.g.
        'albert the great' is returned as 'Albert the Great'."""
    name = name.split()
    new_name = []
    for word in name:
        if word in articles_and_others:
            new_name.append(word)
        else:
            new_name.append(word.capitalize())
    return ' '.join(new_name)

def first_word(string):
     """ Used to retrieve the first string from a menu option presented to the user. This string is then checked
         against the user input to see what option they have chosen."""
     return string.split(' ', 1)[0]


def gen_options_dict(range_of_dict, options):
    """ Used to generate a dict using ints cast to strings as keys, so that there is no need to convert
         the user input to an integer"""
    string_range = [str(num) for num in range_of_dict]

    return dict(zip(string_range, options))


def gen_options(options_list, object_name, action_name, every=True, esc=True):
    """  Takes a list of menu options and returns a dictionary of the form returned by gen_options_dict
         also adds the 'all' and 'exit' option to all menus by default"""
    if not options_list:
        print(f"There are no {object_name}'s to {action_name}.")
        return False

    if every:
        options_list = options_list + ['all']
    if esc:
        options_list = options_list + ['exit']

    return gen_options_dict(range(1, 1 + len(options_list)), options_list)


def print_options(options_dict):
    """ Prints the menu options in a numbered list and returns options_dict to pass to select_options"""
    if not options_dict:
        return False

    for x, option in options_dict.items():
        print(f"{x}: {format_name(option)}")

    print()
    return options_dict


def format_input(selection_string):
    """ Takes any string given by the user, removes extraneous spaces, splits the string
        on the commas and generates a selection list to return"""
    new_str = ''
    prev_char = ''

    for char in selection_string:
        if char != ' ':
            new_str = new_str + char
            prev_char = char
        elif char == ' ' and prev_char != ' ':
            new_str = new_str + char
            prev_char = char
        elif char == ' ' and prev_char == ' ':
            prev_char = char

    new_str = new_str.split(',')
    new_str = [option.strip().lower() for option in new_str]
    return new_str


def select_options(options_to_select, object_name, action_name):
    """ Select_options takes a dictionary of the form returned by print_options, asks the user to choose an option
     or options using either the name of the option or its list number, it then returns a list containing
     all of the options selected in their word form e.g. if the options are {'1':'a','2':'b','3':'c'}
     and the user gives 1, 3, b as input, select_options will return ['a', 'c', 'b'] """
    # Check if there are any options to select from
    if not options_to_select:
        return False

    selection = prompt(f"Which {object_name} would you like to {action_name}? (Please separate options with commas.)")
    selection = format_input(selection)
    options_to_return = []

    # If the user selects 'all' we return a list containing every available option
    # except for 'all' and 'exit'
    all_key = str(len(options_to_select) - 1)
    if options_to_select[all_key] == 'all' and ('all' in selection or all_key in selection):
        # Removes 'exit' and 'all' from the return list
        options_to_return = list(options_to_select.values())
        del options_to_return[-2:]
        return options_to_return

    # returns a list with every option selected by the user in its word form
    # as the words are used as keys later on
    for option in selection:
        if option in options_to_select.keys():
            options_to_return.append(options_to_select[option])
        elif option in options_to_select.values():
            options_to_return.append(option)
        else:
            print("Bad input.")
            print(f"This is what you input: {selection}")
            return select_options(options_to_select, object_name, action_name)

    return options_to_return


def select_options_wrap(options, so_object_name, so_action_name, go_object_name='', 
                       go_action_name='', every=True, esc=True):
    """  select_options_wrap is a wrapper for select_options(print_options(gen_options etc.))
         go_object_name and go_action_name are usually the same as so_object_name and so_action_name
         respectively, but on rare occasions (such as update_knight) they are different."""
    if not go_object_name:
        go_object_name = so_object_name
    if not go_action_name:
        go_action_name = so_action_name
    return select_options(print_options(gen_options(options, go_object_name, go_action_name, every, esc)),
                          so_object_name, so_action_name)








