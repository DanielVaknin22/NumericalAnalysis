import numpy as np


def check_dominant_diagonal(matrix):
    n = len(matrix)
    for i in range(n):
        row_sum = sum(abs(matrix[i, j]) for j in range(n) if i != j)
        if abs(matrix[i, i]) <= row_sum:
            return False
    return True


def jacobi_method(coefficients, constants, max_iterations=1000, tolerance=0.001):
    n = len(constants)
    x = np.zeros(n)
    if not check_dominant_diagonal(coefficients):
        print("No dominant diagonal. Jacobi method cannot be applied.")
        return None

    for _ in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            x_new[i] = (constants[i] - np.dot(coefficients[i, :i], x[:i]) - np.dot(coefficients[i, i + 1:],
                                                                                   x[i + 1:])) / coefficients[i, i]
        if np.allclose(x, x_new, atol=tolerance):
            return x_new
        x = x_new.copy()
    print("Jacobi method did not converge within the specified tolerance.")
    return None


def gauss_seidel_method(coefficients, constants, max_iterations=1000, tolerance=0.001):
    n = len(constants)
    x = np.zeros(n)
    if not check_dominant_diagonal(coefficients):
        print("No dominant diagonal. Gauss-Seidel method cannot be applied.")
        return None

    for _ in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            x_new[i] = (constants[i] - np.dot(coefficients[i, :i], x_new[:i]) - np.dot(coefficients[i, i + 1:],
                                                                                       x[i + 1:])) / coefficients[i, i]
        if np.allclose(x, x_new, atol=tolerance):
            return x_new
        x = x_new.copy()
    print("Gauss-Seidel method did not converge within the specified tolerance.")
    return None


def main():
    coefficients = np.array([[4, -1, 0], [2, 5, -1], [1, 1, 10]], dtype=float)
    constants = np.array([7, 15, -3], dtype=float)

    print("Using Jacobi Method:")
    jacobi_solution = jacobi_method(coefficients, constants)
    if jacobi_solution is not None:
        print("Solution:", jacobi_solution)

    print("\nUsing Gauss-Seidel Method:")
    gauss_seidel_solution = gauss_seidel_method(coefficients, constants)
    if gauss_seidel_solution is not None:
        print("Solution:", gauss_seidel_solution)


if __name__ == "__main__":
    main()
