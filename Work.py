# File: Work.py

# Description: find minimum v with binary search

# Student's Name: Woongchan Lee

# Student's UT EID: WL8863

# Course Name: CS 313E
# Unique Number: 85575

# Date Created: 06/29/2019
# Date Last Modified: 06/29/2019


def binary_search(n, k):
    left = 1
    right = n
    out = 0
    while left <= right:
        v = int(left + (right - left)/2)
        power = 0
        lines = 0
        while v // k**power != 0:
            lines += v // k**power
            power += 1
        if lines >= n:
            out = v
            right = v - 1
        elif lines < n:
            left = v + 1
    return out


def main():
    inf = open("work.txt", "r")
    num_tests = int(inf.readline())
    n = []
    k = []
    for i in range(num_tests):
        test = inf.readline().split(' ')
        n.append(int(test[0]))
        k.append(int(test[1]))
    inf.close()

    # calculate output from binary search
    for i in range(len(n)):
        print(binary_search(n[i], k[i]))


main()
