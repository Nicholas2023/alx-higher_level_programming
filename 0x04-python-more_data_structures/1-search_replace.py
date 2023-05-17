#!/usr/bin/pyhton3
def search_replace(my_list, search, replace):
    new_list = []
    for i, val in enumerate(my_list):
        if val != search:
            new_list.append(val)
        else: 
            my_list[i] = replace
            new_list.append(replace)
        
    return new_list
