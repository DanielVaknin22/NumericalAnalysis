

def print_matrix(matrix):
    for row in matrix:
        print(row)

def matrix_sum(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def matrix_product(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def get_matrix_from_input(prompt):
    print(prompt)
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for row {i+1}, column {j+1}: "))
            row.append(value)
        matrix.append(row)
    return matrix

def main():
    # Get matrices from user input
    matrix1 = get_matrix_from_input("Enter values for Matrix 1:")
    matrix2 = get_matrix_from_input("Enter values for Matrix 2:")

    # A. Print the matrices
    print("\nMatrix 1:")
    print_matrix(matrix1)
    print("\nMatrix 2:")
    print_matrix(matrix2)

    # B. Print the sum of the matrices
    print("\nSum of the matrices:")
    sum_matrices = matrix_sum(matrix1, matrix2)
    print_matrix(sum_matrices)

    # C. Print the product of the matrices
    print("\nProduct of the matrices:")
    product_matrices = matrix_product(matrix1, matrix2)
    print_matrix(product_matrices)

if __name__ == "__main__":
    main()