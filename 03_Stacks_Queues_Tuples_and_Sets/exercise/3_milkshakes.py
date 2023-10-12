from collections import deque

chocolate = deque([int(ch) for ch in input().split(", ")])
milk = deque([int(ch) for ch in input().split(", ")])

count = 0

while True:
    if count == 5:
        break
    elif len(chocolate) == 0 or len(milk) == 0:
        break

    chocolates_ch = chocolate.pop()
    cups_ch = milk.popleft()

    if chocolates_ch <= 0 and cups_ch <= 0:
        continue

    if cups_ch <= 0:
        chocolate.append(chocolates_ch)
        continue

    if chocolates_ch <= 0:
        milk.appendleft(cups_ch)
        continue

    if chocolates_ch == cups_ch:
        count += 1
        continue
    else:
        milk.append(cups_ch)
        chocolates_ch -= 5
        if chocolates_ch <= 0:
            continue
        chocolate.append(chocolates_ch)

if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolate) > 0:
    print(f"Chocolate: {', '.join([str(num) for num in chocolate])}")
else:
    print("Chocolate: empty")

if len(milk) > 0:
    print(f"Milk: {', '.join([str(num) for num in milk])}")
else:
    print("Milk: empty")

    