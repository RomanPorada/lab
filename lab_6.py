matrix = [[19, 62, -45, -1, 84],
          [23, 54, -4, -2, 68],
          [36, 39, 96, 94, 97],
          [-3, -8, -4, -6, -22],
          [98, -5, -3, 0, 11]]

def sort(func):
    def sorted_matrix(matrix):
        sorted_matrix = []
        for matrix_row in matrix:
            ln = len(matrix_row)
            for i in range(ln):
                for j in range(0, ln-i-1):
                    if matrix_row[j] < matrix_row[j + 1]:
                        matrix_row[j], matrix_row[j + 1] = matrix_row[j + 1], matrix_row[j]
            sorted_matrix.append(matrix_row)
        print("Впорядкована матриця:")
        for row in sorted_matrix:
            print(row)
        return func(sorted_matrix)
    return sorted_matrix

@sort
def product_column_elements(matrix):
    ln = len(matrix)
    products = []
    for col in range(ln):
        product = 1
        for row in range(col + 1, ln):
            product *= matrix[row][col]
        if product == 1:
            product = 0
        products.append(product)
    return products

product = product_column_elements(matrix)
print(f"Добуток елементів стовпців матриці що знаходяться під головнобю діагоналю: \n {product}")

sum = 0
for el in product:
    sum += el
arithmetic_average = sum/len(product)

print(f"середнє арефметичне значення добутків елементів стовпців матриці що знаходяться під головнобю діагоналю: \n {arithmetic_average}")