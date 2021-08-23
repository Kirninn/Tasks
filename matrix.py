class Matrix:

    def __init__(self, matrix_string):
        self.matrix_string = [line.split() for line in matrix_string.split('\n')]

    def row(self, index):
        row_list = []
        for item in self.matrix_string[index - 1]:
            row_list.append(item)
        return list(map(int, row_list))
    
    def column(self, index):
        column_list = []
        for item in self.matrix_string:
            column_list.append(item[index - 1])
        return list(map(int, column_list))
