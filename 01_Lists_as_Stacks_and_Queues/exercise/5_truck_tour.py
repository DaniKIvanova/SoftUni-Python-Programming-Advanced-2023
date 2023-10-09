from collections import deque

petrol_pumps = int(input())
petrol_distance = deque()
count = 0

for el in range(petrol_pumps):
    petrol_distance.append([int(ch) for ch in input().split(" ")])

for el in range(petrol_pumps):
    amount = 0
    current_distance = deque()

    for ch in petrol_distance:
        current_distance.append(ch)

    for _ in range(petrol_pumps):
        ch = current_distance.popleft()
        petrol = ch[0]
        needed_petrol = ch[1]

        if (petrol + amount) >= needed_petrol:
            amount += (petrol - needed_petrol)
        else:
            current_distance.append(ch)
            break

    if len(current_distance) == 0:
        print(count)
        break
    else:
        ch = petrol_distance.popleft()
        petrol_distance.append(ch)
        count += 1

