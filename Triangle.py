import time
# File: Triangle.py
# Description: Finds the greatest sum of a path through a number triangle

# Student's Name: Woongchan Lee
# Student's UT EID: WL8863

# Partner's Name: Dohyun Kim
# Partner's UT EID: DK25659

# Course Name: CS 313E
# Unique Number: 85575
# Date Created: 07/02/2019
# Date Last Modified: 07/08/2019

sums = []  # used for exhaustive search algorithm


# returns the greatest path sum using exhaustive search
def exhaustive_search(grid, i=0, j=0, sum=0):
    if i == len(grid):
        sums.append(sum)
    else:
        exhaustive_search(grid, i + 1, j, sum + grid[i][j])
        exhaustive_search(grid, i + 1, j + 1, sum + grid[i][j])


# returns the greatest path sum using greedy approach
def greedy(grid):
    sum = 0
    j = 0
    for i in range(len(grid)):
        if i == len(grid) - 1:
            sum += grid[i][j]
        elif grid[i + 1][j] >= grid[i + 1][j + 1]:
            sum += grid[i][j]
        else:
            sum += grid[i][j]
            j += 1
    return sum


# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search(grid, i=0, j=0):
    if i == len(grid):
        return 0
    left = rec_search(grid, i + 1, j)
    right = rec_search(grid, i + 1, j + 1)
    if left >= right:
        return grid[i][j] + left
    return grid[i][j] + right


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid, memo, i=0, j=0):
    if i == len(grid):
        return 0
    if memo[i][j] != 0:
        return memo[i][j]
    left = rec_search(grid, i + 1, j)
    right = rec_search(grid, i + 1, j + 1)
    if left >= right:
        memo[i][j] = grid[i][j] + left
        return grid[i][j] + left
    memo[i][j] = grid[i][j] + right
    return grid[i][j] + right


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    inf = open("triangle.txt", "r")
    num_rows = int(inf.readline())
    triangle = []
    for num in range(num_rows):
        row_in = inf.readline().split()
        for i in range(len(row_in)):
            row_in[i] = int(row_in[i])
        triangle.append(row_in)
    inf.close()
    return triangle


def main():
    # read triangular grid from file
    triangle = read_file()
    memo = []
    for i in range(len(triangle)):
        row = []
        for j in range(len(triangle[i])):
            row.append(0)
        memo.append(row)

    ti = time.time()
    # output greatest path from exhaustive search
    exhaustive_search(triangle)
    max = 0
    for sum in sums:
        if sum > max:
            max = sum
    print('The greatest path sum through exhaustive search is ' + str(max) + '.')
    tf = time.time()
    del_t = int((tf - ti) * 10 ** 6)
    # print time taken using exhaustive search
    print('The time taken for exhaustive search is ' + str(del_t) + ' microseconds.\n')

    ti = time.time()
    # output greatest path from greedy approach
    sum = greedy(triangle)
    print('The greatest path sum through greedy search is ' + str(sum) + '.')
    tf = time.time()
    del_t = int((tf - ti) * 10 ** 6)
    # print time taken using greedy approach
    print('The time taken for greedy approach is ' + str(del_t) + ' microseconds.\n')

    ti = time.time()
    # output greatest path from divide-and-conquer approach
    sum = rec_search(triangle)
    print('The greatest path sum through recursive search is ' + str(sum) + '.')
    tf = time.time()
    del_t = int((tf - ti) * 10 ** 6)
    # print time taken using divide-and-conquer approach
    print('The time taken for recursive search is ' + str(del_t) + ' microseconds.\n')

    ti = time.time()
    # output greatest path from dynamic programming
    sum = dynamic_prog(triangle,memo)
    print('The greatest path sum through dynamic programming is ' + str(sum) + '.')
    tf = time.time()
    del_t = int((tf - ti) * 10 ** 6)
    # print time taken using dynamic programming
    print('The time taken for dynamic programming is ' + str(del_t) + ' microseconds.\n')


if __name__ == "__main__":
    main()

