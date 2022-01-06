
class Matrix():
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def __add__(self, other):
        matrix_sum = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        # return matrix_sum
        return '\n'.join('\t'.join(map(str, row)) for row in matrix_sum)

    # @property
    # def matrix_proof(self, list_of_lists):
    #     for i in range(len(list_of_lists)):
    #         if len(list_of_lists[i]) != len(list_of_lists[i + 1]):
    #             return f'Incorrect matrix size'
    #
    # @property.setter
    # def term_proof(self, list_of_lists, other):
    #     if len(list_of_lists[0]) != len(other.matrix[0]):
    #         return f'Incorrect matrix size'
    #     if len(list_of_lists) != len(other.matrix):
    #         return f'Incorrect matrix size'


m1 = Matrix([[31, 22], [37, 43]])
m2 = Matrix([[20, 12], [10, 11]])
print(f'Matrix sum equals \n{m2.__add__(m1)} \n')
print(f'Matrix sum equals \n{m1 + m2} \n')
print(f'Matrix is \n{m1} \n')

# m3 = Matrix([2, 3, 4], [8, 9])
# print(m3)

m4 = Matrix([[-1, 64, -8], [3, 5, 8], [8, 3, 7]])
# print(f'Matrix sum equals \n{m1 + m4} \n')

m5 = Matrix([[2, -5, 9], [10, 56, 78], [-8, 90, 35]])
print(f'Matrix sum equals \n{m4 + m5} \n')

m6 = Matrix([[34, 94], [45, -20], [21, -4]])
m7 = Matrix([[87, 32], [-12, -76], [2, 9]])
print(f'Matrix sum equals \n{m6 + m7} \n')