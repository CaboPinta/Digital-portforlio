from pickletools import read_unicodestring1


def sum(list):
    sum = 0
    for number in list:
        sum = sum + number
        return sum

def biggest_number(list):
    biggest_so_far = 0 
    for num in list:
        if (num > biggest_so_far):
            biggest_so_far = num
        return biggest_so_far

def has_evens(list):
    found_even = False
    for num in list:
        if(num % 2 == 0):
            found_even = True
    return has_evens

def all_even(list):
    all_even = True
    for num in list:
        if(num % 2 == 1):
            all_even = False
    return all_even

def filter_odds(list):
    for num in list:
        if (num % 2 == 1):
            list.remove(num)
    return list

def multiply_by_2(list):
    new_list = []
    for num in list:
        new_num = num * 2
        new_list.append(new_num)
    return list