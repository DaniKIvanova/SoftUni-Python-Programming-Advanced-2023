from collections import deque

quantity_of_food = int(input())
sequence_of_orders = [int(ch) for ch in input().split()]

orders_in_queue = deque(sequence_of_orders)
print(max(orders_in_queue))

while len(orders_in_queue) > 0:
    ch = orders_in_queue.popleft()

    if ch <= quantity_of_food:
        quantity_of_food -= ch
    else:
        orders_in_queue.appendleft(ch)
        break

if len(orders_in_queue) > 0:
    print("Orders left:", end=" ")

    for ch in orders_in_queue:
        print(f"{ch}", end=" ")

else:
    print("Orders complete")

