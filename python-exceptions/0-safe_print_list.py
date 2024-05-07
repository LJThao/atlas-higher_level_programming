#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for element in range(x):
            print(my_list[element], end="")
            num += 1
    except IndexError:
        pass
    print()
    return (num)
