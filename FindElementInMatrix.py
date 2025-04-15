sorted_matrix = [
    [1, 2, 4, 7],
    [12, 14, 16, 18],
    [20, 24, 26, 32],
    [34, 36, 38, 42]
]


def search_in_matrix(matrix, tar):
    if not matrix or not matrix[0]:
        return "Not found!"

    rows, cols = len(matrix), len(matrix[0])
    s_row, s_col = [0, cols - 1]

    while s_row < rows and s_col >= 0:
        value = matrix[s_row][s_col]
        if value == tar:
            return [s_row, s_col]
        elif value > tar:
            s_col -= 1
        else:
            s_row += 1

    return "Not found!"


number = int(input("Enter number: "))
result = search_in_matrix(sorted_matrix, number)

for row in sorted_matrix:
    print(row)

print("\nAnswer")
print(result)