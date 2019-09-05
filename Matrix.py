

class Matrix(object):
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        self.matrix = []
        for i in range(row):
            horizontal = []
            for j in range(col):
                horizontal.append(0)
            self.matrix.append(horizontal)

    # perform an assignment operation: matrix[row][col] = data
    def set_element(selfself, row, col, data):
        # if that row and col element already exists