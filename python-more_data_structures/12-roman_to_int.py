#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    sum = 0
    numberals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for char in reversed(roman_string):
        num_value = numberals[char]
        sum += num_value if sum < num_value * 5 else - num_value
    return sum
