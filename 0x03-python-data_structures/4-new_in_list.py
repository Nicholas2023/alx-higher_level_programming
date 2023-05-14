#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''If the index is negative or out of range'''
    list_range = len(my_list) - 1
    if ((idx < 0) or (idx > list_range)):
        return (my_list.copy())
    else:
        '''Create a copy of the original list'''
        '''Replace the elements at a given inddex'''
        new_list = my_list.copy()
        new_list[idx] = element
        return (new_list)
