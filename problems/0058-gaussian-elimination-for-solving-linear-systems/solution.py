import numpy as np

def gaussian_elimination(A, b):
    """
    Solve Ax = b using Gaussian Elimination
    with partial pivoting.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)

    m, n = A.shape
    Ab = np.column_stack((A, b))
    for row in range(m - 1):

        max_row = row

        for i in range(row + 1, m):
            if abs(Ab[i][row]) > abs(Ab[max_row][row]):
                max_row = i

        Ab[[row, max_row]] = Ab[[max_row, row]]

        if abs(Ab[row][row]) < 1e-12:
            raise ValueError("Matrix is singular or has no unique solution")
        for i in range(row + 1, m):

            factor = Ab[i][row] / Ab[row][row]

            Ab[i] = Ab[i] - factor * Ab[row]


    x = np.zeros(n)

    for row in range(n - 1, -1, -1):

        total = 0

        for j in range(row + 1, n):
            total += Ab[row][j] * x[j]

        x[row] = (Ab[row][-1] - total) / Ab[row][row]

    return x


