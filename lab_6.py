matrix = [[19, 62, -45, -1, 84],
          [23, 54, -4, -2, 68],
          [36, 39, 96, 94, 97],
          [-3, -8, -4, -6, -22],
          [98, -5, -3, 0, 11]]

def sort(matrix_rov):
    ln = len(matrix_rov)
    for i in range(ln):
        for j in range(0, ln-i-1):
            if matrix_rov[j] < matrix_rov[j + 1]:
                matrix_rov[j], matrix_rov[j + 1] = matrix_rov[j + 1], matrix_rov[j]
    print(matrix_rov)
    return matrix_rov

print("Впорядкована матриця")
sorted_matrix = [sort(row) for row in matrix]


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

product = product_column_elements(sorted_matrix)
print(f"Добуток елементів стовпців матриці що знаходяться під головнобю діагоналю: \n {product}")


arithmetic_average = sum(product)/len(product)
print(f"середнє арефметичне значення добутків елементів стовпців матриці що знаходяться під головнобю діагоналю: \n {arithmetic_average}")