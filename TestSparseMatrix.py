# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name :Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 07/28/2019
#  Date Last Modified: 07/31/2019

class Link(object):
    def __init__(self, col=0, data=0, next=None):
        self.col = col
        self.data = data
        self.next = next

    # return a String representation of a Link (col, data)
    def __str__(self):
        s = str(self.data)
        return s


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # inserts a link to the end of the list
    def insert_last(self, col, data):
        new_link = Link(col, data)

        current = self.last

        if (current == None):
            self.first = new_link
            self.last = new_link
            self.size += 1
            return

        current.next = new_link
        self.last = new_link
        self.size += 1

    # inserts a link into list in order by column number
    def insert_link(self, col, data):
        new_link = Link(col, data)
        current = self.first
        # checks if list is empty
        if current == None:
            self.first = new_link
            self.last = new_link
            self.size += 1
            return
        # checks if link should go first
        elif current.col > col:
            self.first = new_link
            self.first.next = current
            self.size += 1
            return

        # iterates through list to find correct ordered place
        while current != None:
            # if loop reaches the end of list, add to the end
            if current.next == None:
                current.next = new_link
                self.last = current.next
                self.size += 1
                return
            # if loop reaches a column number larger than input col number, add link
            elif current.next.col > col:
                new_link.next = current.next
                current.next = new_link
                self.size += 1
                return
        return

    # deletes a link
    def delete_link(self, data):
        previous = self.first
        current = self.first

        # return None if list is empty
        if current == None:
            return None

        # iterate through list
        while current != None:
            # if data found condition
            if current.data == data:
                if current == self.first:
                    self.first = self.first.next
                elif current == self.last:
                    self.last = previous
                self.size -= 1
                previous.next = current.next
                return data
            previous = current
            current = current.next
        return None

    # return a String representation of a LinkedList
    def __str__(self):
        s = ''
        current = self.first
        while current != None:
            if s != '':
                s += ' '
            s += str(current)
            current = current.next
        return s


class Matrix(object):
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        self.matrix = []

    # perform an assignment operation: matrix[row][col] = data
    def set_element(self, row, col, data):
        current = self.matrix[row].first
        previous = current
        # do if first list item selected to set
        if current.col == col:
            current.data = data
            # delete link if data is set to 0
            if data == 0:
                self.matrix[row].first = self.current.next
            return data
        # traverse list to find item to set
        while current != None:
            if current.col == col:
                current.data = data
                if data == 0:
                    previous.next = current.next
                return data
            previous = current
            current = current.next
        # if method reaches this point, the link to set has not been found
        # must add a link to the row
        list = self.matrix[row]
        list.insert_last(col, data)
        return data

    # return a linked list representing a row
    def get_row(self, row):
        return self.matrix[row]

    # return a linked list representing a column
    def get_col(self, col):
        new_list = LinkedList()
        for i in range(self.row):
            # search for a column item at index col in the linked list
            found = False
            current = self.matrix[i].first
            while current != None:
                if current.col == col:
                    new_list.insert_last(i, current.data)
                    found = True
                current = current.next
            # if link is not found, add a zero
            if not found:
                new_list.insert_last(i, 0)
        return new_list

    # add two sparse matrices
    def __add__(self, other):
        new_matrix = Matrix(self.row, self.col)
        for row in range(self.row):
            new_row = LinkedList()
            for col in range(self.col):
                # these hold data values at locations [row,col] in their respective matrices
                other_num = 0
                this_num = 0
                # traverse the list to find data values at [row,col]
                other_cur = other.matrix[row].first
                this_cur = self.matrix[row].first
                while other_cur != None:
                    if other_cur.col == col:
                        other_num = other_cur.data
                        break
                    other_cur = other_cur.next
                while this_cur != None:
                    if this_cur.col == col:
                        this_num = this_cur.data
                        break
                    this_cur = this_cur.next
                # sum up data values and add them to the row of the new matrix
                sum = other_num + this_num
                new_row.insert_last(col, sum)
            # add row to matrix
            new_matrix.matrix.append(new_row)
        return new_matrix

    # multiply two sparse matrices
    def __mul__(self, other):
        new_matrix = Matrix(self.row, other.col)
        for row in range(self.row):
            new_row = LinkedList()
            for col in range(other.col):
                sum = 0
                # grab row from this matrix and col from other matrix accordingly
                list1 = self.get_row(row)
                list2 = other.get_col(col)
                # compare and sum up the dot product of the lists
                for op in range(self.col):
                    other_data = 0
                    other_cur = list2.first
                    while other_cur != None:
                        if other_cur.col == op:
                            other_data = other_cur.data
                        other_cur = other_cur.next
                    this_data = 0
                    this_cur = list1.first
                    while this_cur != None:
                        if this_cur.col == op:
                            this_data = this_cur.data
                        this_cur = this_cur.next
                    sum += other_data * this_data
                # add the sum to the row of new matrix
                new_row.insert_last(col, sum)
            # add row to new matrix
            new_matrix.matrix.append(new_row)
        return new_matrix

    # return a String representation of a matrix
    def __str__(self):
        s = ''
        for row in range(self.row):
            line = ''
            # create a list of numbers from the matrix for each row
            list = []
            # fill list with 0's
            for i in range(self.col):
                list.append(0)
            # add numbers to row from linked list
            current = self.matrix[row].first
            while current != None:
                list[current.col] = current.data
                current = current.next
            # add list items to a string
            for item in list:
                if line != '':
                    line += ' '
                line += str(item)
            line += '\n'
            s += line
        return s


def read_matrix(in_file):
    line = in_file.readline().rstrip("\n").split()
    row = int(line[0])
    col = int(line[1])
    mat = Matrix(row, col)

    for i in range(row):
        line = in_file.readline().rstrip("\n").split()
        new_row = LinkedList()
        for j in range(col):
            elt = int(line[j])
            if (elt != 0):
                new_row.insert_last(j, elt)
        mat.matrix.append(new_row)

    line = in_file.readline()

    return mat


def main():
    in_file = open("./matrix.txt", "r")

    print("Test Matrix Addition")
    matA = read_matrix(in_file)
    print(matA)
    matB = read_matrix(in_file)
    print(matB)

    matC = matA + matB
    print(matC)

    print("\nTest Matrix Multiplication")
    matP = read_matrix(in_file)
    print(matP)
    matQ = read_matrix(in_file)
    print(matQ)

    matR = matP * matQ
    print(matR)

    print("\nTest Setting a Zero Element a Non-Zero Value")
    matA.set_element(1, 1, 5)
    print(matA)

    print("\nTest Setting a Non-Zero Element to a Zero Value")
    matB.set_element(1, 1, 0)
    print(matB)

    print("\nTest Getting a Row")
    row = matP.get_row(1)
    print(row)

    print("\nTest Getting a Col")
    col = matQ.get_col(0)
    print(col)

    in_file.close()


main()

