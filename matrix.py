class Matrix:

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        if '\n' in self.matrix_string:
            self.index_long = self.matrix_string.replace(' ', '').index('\n')
        self.matrix_string = self.matrix_string.replace('\n', ' ').split(' ')


    def row(self, index):
        list_row = []
        if len(self.matrix_string) == 1:
            for item in self.matrix_string:
                list_row.append(int(item))
            return list_row

        if len(self.matrix_string) == 4:
            if index == 1:
                for item in self.matrix_string[:2]:
                    list_row.append(int(item))
                return list_row
            if index == 2:
                for item in self.matrix_string[2:4]:
                    list_row.append(int(item))
                return list_row

        if len(self.matrix_string) == 9:
            if index == 1:
                for item in self.matrix_string[:3]:
                    list_row.append(int(item))
                return list_row

            if index == 2:
                for item in self.matrix_string[3:6]:
                    list_row.append(int(item))
                return list_row

            if index == 3:
                for item in self.matrix_string[6:9]:
                    list_row.append(int(item))
                return list_row

        if len(self.matrix_string) == 12 and self.index_long == 4:
            if index == 1:
                for item in self.matrix_string[:4]:
                    list_row.append(int(item))
                return list_row

            if index == 2:
                for item in self.matrix_string[4:8]:
                    list_row.append(int(item))
                return list_row

            if index == 3:
                for item in self.matrix_string[8:12]:
                    list_row.append(int(item))
                return list_row

        if len(self.matrix_string) == 12 and self.index_long == 3:
            if index == 1:
                for item in self.matrix_string[:3]:
                    list_row.append(int(item))
                return list_row

            if index == 2:
                for item in self.matrix_string[3:6]:
                    list_row.append(int(item))
                return list_row

            if index == 3:
                for item in self.matrix_string[6:9]:
                    list_row.append(int(item))
                return list_row

            if index == 4:
                for item in self.matrix_string[9:12]:
                    list_row.append(int(item))
                return list_row

    def column(self, index):
        list_coium = []

        if len(self.matrix_string) == 1:
            for item in self.matrix_string[::2]:
                list_coium.append(int(item))
            return list_coium

        if len(self.matrix_string) == 4:
            if index == 1:
                for item in self.matrix_string[::2]:
                    list_coium.append(int(item))
                return list_coium

            if index == 2:
                for item in self.matrix_string[1::2]:
                    list_coium.append(int(item))
                return list_coium

        if len(self.matrix_string) == 9:
            if index == 1:
                for item in self.matrix_string[::3]:
                    list_coium.append(int(item))
                return list_coium

            if index == 2:
                for item in self.matrix_string[1::3]:
                    list_coium.append(int(item))
                return list_coium

            if index == 3:
                for item in self.matrix_string[2::3]:
                    list_coium.append(int(item))
                return list_coium   
                
        if len(self.matrix_string) == 12 and self.index_long == 3:
            
            if index == 1:
                for item in self.matrix_string[::3]:
                    list_coium.append(int(item))
                return list_coium

            if index == 2:
                for item in self.matrix_string[1::3]:
                    list_coium.append(int(item))
                return list_coium

            if index == 3:
                for item in self.matrix_string[2::3]:
                    list_coium.append(int(item))
                return list_coium

        if len(self.matrix_string) == 12 and self.index_long == 4:

            if index == 1:
                for item in self.matrix_string[::4]:
                    list_coium.append(int(item))
                return list_coium

            if index == 2:
                for item in self.matrix_string[1::4]:
                    list_coium.append(int(item))
                return list_coium

            if index == 3:
                for item in self.matrix_string[2::4]:
                    list_coium.append(int(item))
                return list_coium  

            if index == 4:
                for item in self.matrix_string[3::4]:
                    list_coium.append(int(item))
                return list_coium
