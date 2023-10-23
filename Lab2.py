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


def calc_median(numbers):
    sorted_readings = sorted(numbers)
    num_readings = len(sorted_readings)
    if num_readings %2 == 1:
        median = sorted_readings[num_readings//2]
    else:
        middle1 = sorted_readings[num_readings // 2 - 1]
        middle2 = sorted_readings[num_readings // 2]
        median = (middle1 + middle2) / 2
    return median



user_input_list = get_user_input()
average = calc_average(user_input_list)
min_max = calc_min_max(user_input_list)
median = calc_median(user_input_list)

print(f"Average: {average:.2f}")
print(f"Minimum: {min_max[0]}")
print(f"Maximum: {min_max[1]}")
print(f"Median: {median:.2f}")