
#  File: MagicSquare.py
#  Description: Take user input to create a n-sized magic square and check if program created magic square correctly

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: dk25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 06/15/2019
#  Date Last Modified: 06/15/2019
#  Extra Credit: Writing extra function to create a print_square function that can print any sized square with
#  correct right aligned spacing while also following Python conventions and commenting code


# Return number of digits of number num
def num_digits(num):
    count = 0
    n = int(num)
    while n / 10 > 0:
        count += 1
        n = n // 10
    return count


# Print the magic square in a neat format where the numbers are right justified
def print_square(magic_square):
    print("Here is a " + str(len(magic_square)) + " x " + str(len(magic_square)) + " magic square: \n")
    numdig = num_digits(len(magic_square) ** 2)
    for row in range(len(magic_square)):
        string = ""
        for col in range(len(magic_square)):
            if col != 0:
                string += " "
            string += "{:>{x}}".format(magic_square[row][col], x=numdig)
        print(string)
    print()


# Populate a 2-D list with numbers from 1 to n2
def make_square(n):
    grid = []
    i = 0
    while i < n:  # create grid of size n * n full of zeroes
        row = []
        j = 0
        while j < n:
            row.append(0)
            j += 1
        grid.append(row)
        i += 1
    max_value = n * n
    count = 1  # loop will increment and add this value to magic square
    i = n - 1
    j = int(n / 2)  # starting position for magic square
    while count <= max_value:
        grid[i][j] = count
        count += 1
        i += 1  # move to next location
        j += 1
        if i == n and j == n:
            i -= 2  # move up if next location is in the outside corner
            j -= 1
        elif i == n:
            i = 0  # move to first row if next location is outside on bottom side of magic square
        elif j == n:
            j = 0  # move to first column if next location is outside on right side of magic square
        elif grid[i][j] != 0:
            i -= 2  # move up if next location is already occupied
            j -= 1
    return grid


# Check that the 2-D list generated is indeed a magic square
def check_square(magic_square):
    n = len(magic_square)
    actual_sum = int(n * (n**2 + 1) / 2)
    sum_row = 0
    sum_col = 0
    sum_diag_ul = 0
    sum_diag_ur = 0

    for i in range(len(magic_square)):  # add up sums for rows and diagonals
        sum_row = 0
        for j in range(len(magic_square)):
            sum_row += magic_square[i][j]
            if i == j:
                sum_diag_ul += magic_square[i][j]
            if i + j == len(magic_square)-1:
                sum_diag_ur += magic_square[i][j]
        if sum_row != actual_sum:
            break

    for j in range(len(magic_square)):  # add up sums for columns
        sum_col = 0
        for i in range(len(magic_square)):
            sum_col += magic_square[i][j]
        if sum_col != actual_sum:
            break

    if (actual_sum != sum_row) or (actual_sum != sum_row) or (actual_sum != sum_row) or (actual_sum != sum_row):
        print("Not a magic square! Actual sum should be = " + str(actual_sum))  # print actual sum if not a magic square
    else:
        print("Sum of row = " + str(sum_row))  # print out sums if it is a magic square
        print("Sum of column = " + str(sum_col))
        print("Sum diagonal (UL to LR) = " + str(sum_diag_ul))
        print("Sum diagonal (UR to LL) = " + str(sum_diag_ur))


def main():
    print("Please enter an odd number:", end=" ")
    n = int(input())
    while n < 3 or n % 2 == 0:  # ask for input if n is not big enough or n is even
        print("Please enter an odd number:", end=" ")
        n = int(input())
    print()
    magic_square = make_square(n)
    print_square(magic_square)
    check_square(magic_square)


main()
