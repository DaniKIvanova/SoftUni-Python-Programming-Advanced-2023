square_matrix = []
rows = int(input())

for el in range(rows):
    square_matrix.append([int(ch) for ch in input().split(", ")])

primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
    primary_diagonal.append(square_matrix[i][i])
    secondary_diagonal.append(square_matrix[i][rows - 1 - i])

print(f"Primary diagonal: {', '.join(str(ch) for ch in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(ch) for ch in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

