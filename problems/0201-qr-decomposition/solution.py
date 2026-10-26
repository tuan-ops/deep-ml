
import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    A = np.array(A, dtype=float)

    if A.ndim != 2 or A.shape[0] == 0 or A.shape[1] == 0:
        raise ValueError("A must be a non-empty 2D matrix")

    m, n = A.shape

    if m < n:
        raise ValueError("QR decomposition requires m >= n")

    R = np.zeros((n, n), dtype=float)
    Q = np.zeros((m, n), dtype=float)
    V = A.copy()

    for j in range(n):
        R[j, j] = np.linalg.norm(V[:, j])

        if np.isclose(R[j, j], 0.0):
            raise ValueError("The columns of A are linearly dependent")

        Q[:, j] = V[:, j] / R[j, j]

        for k in range(j + 1, n):
            R[j, k] = np.dot(Q[:, j], V[:, k])
            V[:, k] -= R[j, k] * Q[:, j]

    return Q.tolist(), R.tolist()
