rows, columns = (int(ch) for ch in input().split(" "))

final_matrix = []

for row in range(rows):
    current_matrix = []

    for cols in range(columns):
        first_ch, third_ch = chr(97 + row), chr(97 + row)
        second_ch = chr(97 + row + cols)
        current_matrix.append(first_ch + second_ch + third_ch)
    final_matrix.append(current_matrix)

for i in range(len(final_matrix)):
    print(*final_matrix[i])
