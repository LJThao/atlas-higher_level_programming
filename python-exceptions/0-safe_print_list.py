#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for element in range(x):
        try:
            print(f"{my_list[element]}", end="")
            num += 1
        except IndexError:
            break
        print()
        return(num)
