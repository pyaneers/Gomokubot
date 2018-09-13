# write me a function that takes in a list of 25 elements (ml)
# and returns a 2d array of 5 elements (db)

# and another in reverse


def DBML_parser(matrix):
    """
    turns a 2d list into a list
    """
    return_series = []
    for row in matrix:
        for item in row:
            return_series.append(item)

    return return_series


def MLDB_parser(series):
    """
    turns a list into a 2d list
    """
    return_matrix = []
    matrix_row = []

    for item in series:
        matrix_row.append(item)
        if len(matrix_row) == 5:
            return_matrix.append(matrix_row)
            matrix_row = []

    return return_matrix


# m = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
# s = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# DBML_parser(m)

# MLDB_parser(s)
