def create_matrix(n_lines):
    result = []
    for _ in range(n_lines):
        result.append([int(el) for el in input().split()])
    return result


def print_result(sum_one, sum_two):
    result = abs(sum_one - sum_two)
    print(result)


n = int(input())
matrix = create_matrix(n)

sum_diagonal_one = 0
sum_diagonal_two = 0

for i in range(n):
    sum_diagonal_one += matrix[i][i]
    sum_diagonal_two += matrix[i][n - 1 - i]

print_result(sum_diagonal_one, sum_diagonal_two)
