#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for x in matrix:
        new.append([y * y for y in x])
    return new
