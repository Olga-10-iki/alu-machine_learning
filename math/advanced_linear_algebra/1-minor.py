#!/usr/bin/env python3
"""
Module that computes the minor matrix of a square matrix.
"""


def determinant(matrix):
    """
    Computes the determinant of a square matrix.
    """

    if matrix == [[]]:
        return 1

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    det = 0

    for col in range(n):
        minor = [
            [matrix[i][j] for j in range(n) if j != col]
            for i in range(1, n)
        ]

        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


def minor(matrix):
    """
    Computes the minor matrix of a square matrix.
    """

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    if n == 1:
        return [[1]]

    result = []

    for i in range(n):
        row = []

        for j in range(n):
            sub = [
                [matrix[r][c] for c in range(n) if c != j]
                for r in range(n) if r != i
            ]

            row.append(determinant(sub))

        result.append(row)

    return result
