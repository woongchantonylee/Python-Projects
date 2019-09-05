
#  File: WordSearch.py
#  Description: Given the dimensions of
#  the word search puzzle and the number
#  of words to find, search the puzzle
#  and write the coordinates of the first letter

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: dk25659

#  Course Name: CS 313E 
#  Unique Number: 85575
#  Date Created: 06/10/2019
#  Date Last Modified: 06/14/2019
#  Extra Credit: Use of recursion and following Python conventions


# Read Input Matrix and given words
def get_words(inf):
    line = inf.readline()
    matrix = line.split()  # read dimensions

    string = []
    count = 0
    line = inf.readline()
    while count < int(matrix[0]):  # read characters in puzzle
        line = inf.readline()
        character = line.split()
        string.append(character)
        count += 1

    line = inf.readline()
    line = inf.readline()
    numb_words = int(line)

    words = []
    count = 0
    line = inf.readline()
    while count < numb_words:  # read wordbank
        arr = list(line)
        if arr[-1] == "\n":
            del arr[-1]
        words.append(arr)
        line = inf.readline()
        count += 1
        
    return string, words  # return puzzle and wordbank


# Checks if word exists in top-left direction
def top_left(list_char, word_search, i, j, string_index):
    if string_index == len(list_char):
        return True
    if i < 0 or j < 0:
        return False  # end recursion if indices point out of bounds
    # continue iterating if next letter exists in current index
    if list_char[string_index] == word_search[i][j]:
        return top_left(list_char, word_search, i - 1, j-1, string_index+1)
    return False


# Checks if word exists in upward direction
def top_center(list_char, word_search, i, j, string_index):
    if string_index == len(list_char):
        return True  # word checks out if all letters accounted fore
    if i < 0:
        return False  # end recursion if indices point out of bounds
    # continue iterating if next letter exists in current index
    if list_char[string_index] == word_search[i][j]:
        return top_center(list_char, word_search, i - 1, j, string_index+1)
    return False


# Checks if word exists in top-right direction
def top_right(list_char, word_search, i, j, string_index):
    if string_index == len(list_char):
        return True  # word checks out if all letters accounted for
    if i < 0 or j >= len(word_search[i]):
        return False  # end recursion if indices point out of bounds
    # continue iterating if next letter exists in current index
    if list_char[string_index] == word_search[i][j]:
        return top_right(list_char, word_search, i - 1, j + 1, string_index+1)
    return False


# Checks if word exists in right direction
def right(list_char, word_search, i, j, string_index):
    if string_index == len(list_char):
        return True  # word checks out if all letters accounted for
    if j >= len(word_search[i]):
        return False  # end recursion if indices point out of bounds
    # continue iterating if next letter exists in current index
    if list_char[string_index] == word_search[i][j]:
        return right(list_char, word_search, i, j + 1, string_index + 1)
    return False


# Checks if word exists in left direction
def left(list_char, word_search, i, j, string_index):
    if string_index == len(list_char):
        return True  # word checks out if all letters accounted for
    if j < 0:
        return False  # end recursion if indices point out of bounds
    # continue iterating if next letter exists in current index
    if list_char[string_index] == word_search[i][j]:
        return left(list_char, word_search, i, j - 1, string_index + 1)
    return False


# Checks if word exists in bot-left direction
def bot_left(list_char, word_search, i, j, string_index):
    if string_index == len(list_char):
        return True  # word checks out if all letters accounted for
    if i >= len(word_search) or j < 0:
        return False  # end recursion if indices point out of bounds
    # continue iterating if next letter exists in current index
    if list_char[string_index] == word_search[i][j]:
        return bot_left(list_char, word_search, i + 1, j - 1, string_index + 1)
    return False


# Checks if word exists in downward direction
def bot_center(list_char, word_search, i, j, string_index):
    if string_index == len(list_char):
        return True  # word checks out if all letters accounted for
    if i >= len(word_search):
        return False  # end recursion if indices point out of bounds
    # continue iterating if next letter exists in current index
    if list_char[string_index] == word_search[i][j]:
        return bot_center(list_char, word_search, i + 1, j, string_index + 1)
    return False


# Checks if word exists in bot_right direction
def bot_right(list_char, word_search, i, j, string_index):
    if string_index == len(list_char):
        return True  # word checks out if all letters accounted for
    if i >= len(word_search) or j >= len(word_search[i]):
        return False  # end recursion if indices point out of bounds
    # continue iterating if next letter exists in current index
    if list_char[string_index] == word_search[i][j]:
        return bot_right(list_char, word_search, i + 1, j + 1, string_index + 1)
    return False


# Starts branching in all directions to see if word exists
def start_branch(list_char, word_search, i, j, string_index):
    if (top_left(list_char, word_search, i-1, j-1, string_index+1) or
            top_center(list_char, word_search, i-1, j, string_index+1) or
            top_right(list_char, word_search, i-1, j+1, string_index+1) or
            right(list_char, word_search, i, j+1, string_index+1) or
            left(list_char, word_search, i, j-1, string_index+1) or
            bot_left(list_char, word_search, i+1, j-1, string_index+1) or
            bot_center(list_char, word_search, i+1, j, string_index+1) or
            bot_right(list_char, word_search, i+1, j+1, string_index+1)):
        return True, i, j
    return False, 0, 0


# iterates through puzzle and returns coordinates of found words
def find_words(values):
    output = []
    h = 0
    while h < len(values[1]):
        string_index = 0
        i = 0
        out_unit = []
        string = ""
        while i < len(values[1][h]):
            string += str(values[1][h][i])
            i += 1
        out_unit.append(string)
        out_unit.append(0)
        out_unit.append(0)
        output.append(out_unit)  # output default to string and (0,0) coordinates
        i = 0
        while i < len(values[0]):  # iterate through matrix for the first letter of string
            j = 0
            while j < len(values[0][i]):
                # if first letter is found, start branching to see if string exists in current location
                if values[1][h][string_index] == values[0][i][j]:
                    coor = start_branch(values[1][h], values[0], i, j, string_index)
                    if coor[0]:  # if word is found, update output
                        output[h][1] = coor[1] + 1
                        output[h][2] = coor[2] + 1
                j += 1
            i += 1
        h += 1
    return output


# print word with its row and column number in the puzzle
def print_output(output, fh):
    max = 0
    i = 0
    # determine largest word length
    while i < len(output):
        if len(output[i][0]) > max:
            max = len(output[i][0])
        i += 1
    i = 0
    while i < len(output):
        space = (max+4) - len(output[i][0])  # use word length to determine spacing
        fh.write(output[i][0] + " {:>{x}}".format(output[i][1], x=space) + " {:>4}".format(output[i][2]) + "\n")
        i += 1


def main():
    inf = open("hidden.txt", "r")
    values = get_words(inf)  # read input from hidden.txt
    inf.close()
    fh = open("found.txt", "w")
    output = find_words(values)  # determine output values
    print_output(output, fh)  # write output to found.txt
    fh.close()


main()
