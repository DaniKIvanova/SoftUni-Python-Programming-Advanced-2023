from collections import deque

clothes_curnt = [int(ch) for ch in input().split(" ")]
clothes = deque(clothes_curnt)
racks = int(input())
curnt_racks = racks
count = 1

while clothes:
    ch = clothes.pop()

    if curnt_racks == 0:
        count += 1
        curnt_racks = racks

    if ch <= curnt_racks:
        curnt_racks -= ch
    elif ch > curnt_racks:
        count += 1
        curnt_racks = racks
        curnt_racks -= ch

print(count)

