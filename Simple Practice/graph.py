def row_with_max_ones(mat):
    if not mat or not mat[0]:
        return -1, 0

    R, C = len(mat), len(mat[0])

    # start at top-right
    r, c = 0, C - 1
    max_row = -1

    while r < R and c >= 0:
        if mat[r][c] == 1:
            max_row = r       # this row has at least (C - c) ones
            c -= 1            # try to find an even earlier 1 (more ones)
        else:
            r += 1            # move down to next row

    if max_row == -1:
        return -1, 0

    ones_count = C - (c + 1)  # because c stopped one step left of the leftmost 1
    return max_row, ones_count


# Example
mat = [
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1]
]

row, ones = row_with_max_ones(mat)
print("Row with max 1s:", row)
print("Number of 1s:", ones)


