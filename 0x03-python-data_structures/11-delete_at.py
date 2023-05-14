#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_range = len(my_list) - 1
    if (idx < 0) or (idx > list_range):
        return (my_list)
    else:
        my_list.remove(my_list[idx])
    return (my_list)
