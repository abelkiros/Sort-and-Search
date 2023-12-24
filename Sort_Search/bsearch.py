"""
file: bsearch.py
language: python3
author: amk7296@g.rit.edu abel m kiros
description: Binary search algorithm
"""

def binary_search(data, target, start, end):

    if start > end:

        return None

    mid_index = (start + end) // 2
    mid_value = data[mid_index]

    print("Search for", target, ":", data[start:mid_index], "*" + str(mid_index) + "*", data[mid_index+1: end +1])

    if target == mid_value:
        return mid_value

    elif target < mid_value:
        return binary_search(data, target, start, mid_index-1)
    else:
        return binary_search(data, target, mid_index+1, end)

def get_index(data, target):

    return binary_search(data, target, 0, len(data)-1)

def main():

    start = int(input("Start: "))
    stop = int(input("Stop: "))
    step = int(input("Step: "))

    data = []
    for loop in range(start, stop, step):
        data +=[loop]

    print("\nData: ", data)
    print("Number of elements: ", len(data))

    print("\nStep 2 - Enter target value to search for..." )
    target = int( input("Target: "))

    print("\nStep 3- Get index of target value in data (None if doesn't exist)...")
    index = get_index(data, target)
    print()
    if index != None:
        print(target, "found at index", index)
    else:
        print(target, "not found")

main()