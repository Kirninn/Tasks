class Matrix:

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_string = [list(line) for line in self.matrix_string.splitlines()]

    def row(self, index):
        row_list = []
        for item in self.matrix_string[index - 1]:
            if item == ' ':
                pass
            else:
                row_list += item
        return list(map(int, row_list))
    
    def column(self, index):
        column_list = []
        for item in self.matrix_string:
            column_list += item[index - 1][index - 1]
        return list(map(int, column_list))
            
c = Matrix('10 20 30\n4 5 6')

print(c.row(1))
