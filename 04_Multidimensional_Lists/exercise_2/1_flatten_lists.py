nums = [numbers.split() for numbers in input().split("|")]

for ch in nums[::-1]:
    [print(chart, end=" ") for chart in ch]
