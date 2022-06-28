# coding=utf-8
import re


def string_to_list(st):
    """
    Question1: Covert a string to a list
    :param st: string to be coverted
    :return: expected list
    """
    st_lower = st.lower()  # string内建函数实现大小写转换
    st_char = st_lower.strip('.')   # string内建函数剥离标点符号
    st_list = st_char.split(" ")   # string内建函数分割字符串
    return st_list


def find_numbers(st):
    """
    Question 2: find numbers in a string.
    :param st: input string
    :return: number list
    """
    pattern = r"\d+"
    result = re.findall(pattern, st)
    return result


def list_unique(lst):
    """
    Question 3: remove the redundant elements in a list
    :param lst: the objective list
    :return: a new list
    """
    new_lst = []
    [new_lst.append(element) for element in lst if element not in new_lst]
    return new_lst


def step2(start, end, step=2):
    """
    Question 4: define a function which can go through be step 2
    :param start:
    :param end:
    :param step:
    :return:
    """
    beg = start
    while beg < end:
        yield beg
        beg += step


if __name__ == '__main__':
    st = "This is a Python test."
    st_to_list = string_to_list(st)
    print(st_to_list)
    find_numbers("Bob is 16 years old and his sister is 18.")
    new_lst = list_unique([1, 2, 3, 3, 4, 4, 4, 5])
    print(new_lst)
    for item in step2(0, 10):
        print(item)
