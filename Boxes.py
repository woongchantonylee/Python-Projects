
#  File: Boxes.py
#  Description: Finds the largest subset of boxes that fit in one another

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 07/12/2019
#  Date Last Modified: 07/12/2019

# Contains all legitimate nestings of box sets
all_nestings = []


def find_sub_sets(a, b, idx):
    if idx == len(a):
        all_nestings.append(b)
        return
    else:
        c = b[:]
        b.append(a[idx])
        if len(b) > 1 and (b[len(b) - 1][0] <= b[len(b) - 2][0] or b[len(b) - 1][1] <= b[len(b) - 2][1] or
                           b[len(b) - 1][2] <= b[len(b) - 2][2]):
            find_sub_sets(a, c, idx + 1)
        else:
            find_sub_sets(a, b, idx + 1)
            find_sub_sets(a, c, idx + 1)


def read_in():
    # Read input from boxes.txt and store into 2D list
    inf = open("boxes.txt", "r")
    num_boxes = int(inf.readline())
    boxes = []
    for num in range(num_boxes):
        row_in = inf.readline().split()
        for i in range(len(row_in)):
            row_in[i] = int(row_in[i])
        row_in.sort()
        boxes.append(row_in)
    inf.close()
    return boxes


def main():
    box_sizes = read_in()
    box_sizes.sort()
    box_set = []
    # Recurse and find all legitimate subsets
    find_sub_sets(box_sizes, box_set, 0)
    max_num_nested = 0
    nests = []
    # Determine from all legitimate nestings what the largest subset
    for nesting in all_nestings:
        for i in range(len(nesting) - 1):
            if nesting[i][0] >= nesting[i+1][0] or nesting[i][1] >= nesting[i+1][1] or nesting[i][2] >= nesting[i+1][2]:
                # If nesting is illegitimate, exit loop
                break
            if i == len(nesting) - 2 and len(nesting) > max_num_nested:
                # A new largest subset was found. Clear current subsets and update max number and nests
                nests.clear()
                max_num_nested = len(nesting)
                nests.append(nesting)
            elif i == len(nesting) - 2 and len(nesting) == max_num_nested:
                # Another subset with same length as maximum was found
                nests.append(nesting)
    if max_num_nested < 2:
        # No boxes are nested if nests are only size 1 or 0
        print("No Nesting Boxes")
    else:
        # Print out all sets of maximum number of boxes nested
        print("Largest Subset of Nesting Boxes")
        for nest in nests:
            for box in nest:
                print(box)
            print()


if __name__ == "__main__":
    main()

