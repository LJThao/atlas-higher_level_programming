#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def replace_if_match(element):
        return element if element != search else replace
    return list(map(replace_if_match, my_list))
