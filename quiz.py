import random

# this is the menu where u choose what you would like to do
def display_intro():
    title = "!! Herbs Math Quiz !!"
    print("!" * len(title))
    print(title)
    print("!" * len(title))


def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])


def display_separator():
    print("-" * 24)


def get_user_input():
    user_input = int(input("Enter your choice (MUST BE A NUMBER) : "))
    while user_input > 5 or user_input <= 0:
        print("Incorrect menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input

# this is where you type your answer to the question
def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result

# this is where your answer is checked to see if it is correct
def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Yessir.")
        return count
    else:
        print("Nope.")
        return count

# this is where the questions are generated
def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if index is 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 3:
        problem = str(number_one) + " * " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count

# this is where your score is rounded
def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Bye Bye.", sep = "")


def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 4:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

# here is the exit code
    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)

main()
