def get_float_input(prompt, error_message="Enter float value: "):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(error_message)


def get_integer_input(prompt, error_message="Enter integer value: "):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(error_message)


def get_string_input(prompt):
    return input(prompt)

def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ["yes", "no"]:
            return choice
        else:
            print("Error! Please enter 'yes' or 'no'.")