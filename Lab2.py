print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to python")


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    display_main_menu()
    user_input = input()
    numbers_as_strings = user_input.split(",")
    numbers_as_floats = [float(num) for num in numbers_as_strings]
    return numbers_as_floats


def calc_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


def calc_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return [minimum, maximum]


user_input_list = get_user_input()
average = calc_average(user_input_list)
min_max = calc_min_max(user_input_list)

print(f"Average: {average:.2f}")
print(f"Minimum: {min_max[0]}")
print(f"Maximum: {min_max[1]}")