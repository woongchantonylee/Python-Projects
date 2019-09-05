
#  File: Queens.py
#  Description: Simulates old queen puzzle and prints out number of possible solutions depending on size of board

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 07/12/2019
#  Date Last Modified: 07/12/2019


class Queens (object):
    # initialize the board
    def __init__(self, n=8):
        self.board = []
        self.n = n
        self.num_solutions = 0
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()
        print()

    # check if no queen captures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do a recursive backtracking solution
    def recursive_solve(self, col):
        if col == self.n:
            # Base case
            # self.print_board()
            self.num_solutions += 1
        else:
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'
                    self.recursive_solve(col + 1)
                    self.board[i][col] = '*'

    # if the problem has a solution print the board
    def solve(self):
        self.recursive_solve(0)
        print('\nNumber of solutions:', self.num_solutions)


def main():
    num_size = int(input('Enter the size of board: '))
    while num_size < 1 or num_size > 16:
        num_size = int(input('Enter the size of board: '))
    # create a chess board
    game = Queens(num_size)

    # place the queens on the board
    game.solve()


main()

