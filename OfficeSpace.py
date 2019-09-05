
#  File: OfficeSpace.py
#  Description: Reads offices and employee spaces and calculates spaces for everyone and contested spaces

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 06/17/2019
#  Date Last Modified: 06/17/2019
#  Extra Credit: Using object-oriented programming to create Office objects and using 2-D lists to calculate areas


class Office(object):

    # Constructor with office space initialized with zeroes
    def __init__(self, row=1, col=1):
        self.office_space = []
        for i in range(row):
            row = []
            for j in range(col):
                row.append(int(0))
            self.office_space.append(row)
        self.name = []
        self.name_ind = 0

    # Add an employee office to list of names and fill in area of the space in the 2-D list
    def add_office(self, name, i, j, maxi, maxj):
        self.name.append(name)  # Add name to list
        self.name_ind += 1  # increment fill number
        maxi -= 1
        maxj -= 1
        jreset = j
        while i <= maxi:
            j = jreset
            while j <= maxj:
                if self.office_space[i][j] == 0:
                    self.office_space[i][j] = self.name_ind
                else:
                    self.office_space[i][j] = 50  # mark space as contested if space already filled
                j += 1
            i += 1

    # When printing out the object, it should print everything out in correct format
    def __str__(self):
        out = "Total " + str(len(self.office_space) * len(self.office_space[0]))
        empty = 0
        contested = 0
        for i in range(len(self.office_space)):
            for j in range(len(self.office_space[i])):
                if self.office_space[i][j] == 0:
                    empty += 1
                if self.office_space[i][j] == 50:
                    contested += 1
        out += "\nUnallocated " + str(empty)
        out += "\nContested " + str(contested)
        for h in range(self.name_ind):
            out += "\n" + self.name[h] + " "
            space = 0
            for i in range(len(self.office_space)):
                for j in range(len(self.office_space[i])):
                    if self.office_space[i][j] == (h + 1):
                        space += 1
            out += str(space)
        out += "\n"
        return out


def main():
    inf = open("office.txt", "r")
    offices = []
    i = 0

    # Read all lines and fill them into offices lists
    line = inf.readline()
    dimen = line.split()  # read dimensions
    while len(dimen) != 0:
        offices.append(Office(int(dimen[0]), int(dimen[1])))
        line = inf.readline()
        num_employees = int(line)
        for j in range(num_employees):
            line = inf.readline()
            employee = line.split()
            offices[i].add_office(employee[0], int(employee[1]), int(employee[2]), int(employee[3]), int(employee[4]))
        i += 1
        line = inf.readline()
        dimen = line.split()  # read dimensions

    inf.close()
    for office in offices:
        print(office)


main()
