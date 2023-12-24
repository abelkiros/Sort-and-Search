"""
file: selectionsort.py
language: python3
author: amk7296@g.rit.edu abel m kiros
description: Selection Sorting algorithm
"""

def readfile(file):
    """This function reads the file line by line and stores it as a list

    :param file: Is the text file the user selects
    :return: A list of numbers
    """
    with open(file) as f:

        lst = []

        for line in f:

            for i in line.strip().split():

                lst.append(i)

        return lst


def findMaxFrom(lst, mark):
    """This function compares the sizes of lst and mark
    """
    for index in range(mark+1, len(lst)):

        if lst[mark] > lst[index]:

            mark = index

    return mark


def swap(lst, mark, index):
    """This function swaps the postion of lst and mark"""
    value = lst[mark]

    lst[mark] = lst[index]

    lst[index] = value


def selectionSort(lst):
    """This function sorts a list

    :param lst: Takes in the a list
    :return: The list is sorted from Max to Min
    """
    for mark in range(0, len(lst)-1):

        swap(lst, mark, findMaxFrom(lst, mark))

def main():
    """The main function takes the user input and calls the sort & readfile functions
    """
    user_input = input("Enter file name: ")
    lst = readfile(user_input)
    print("Sorting File: ", user_input)
    print("unsorted: ", lst)
    selectionSort(lst)
    print("sorted: ", lst)

main()