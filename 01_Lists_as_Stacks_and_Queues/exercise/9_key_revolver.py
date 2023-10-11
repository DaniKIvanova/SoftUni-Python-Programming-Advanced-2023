from collections import deque

price_of_bullet = int(input())
size_gun_barrel = int(input())
bullets_list = [int(ch) for ch in input().split(" ")]
bullets = deque(bullets_list)
list_locks = [int(ch) for ch in input().split(" ")]
locks = deque(list_locks)
money_earned = int(input())
count = 0

while len(bullets) > 0 and len(locks) > 0:
    current_bullets = bullets.pop()
    current_locks = locks.popleft()

    if current_bullets <= current_locks:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_locks)

    count += 1
    money_earned -= price_of_bullet
    if size_gun_barrel == count and len(bullets) > 0:
        print("Reloading!")
        count = 0

if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

