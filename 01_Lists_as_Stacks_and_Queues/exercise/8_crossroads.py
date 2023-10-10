from collections import deque

green_light = int(input())
free_window = int(input())
traffic_queue = deque()
total_cars_passed = 0
car = ""
character_hit = ""

while True:
    command = input()
    current_green = green_light
    current_free = free_window

    if command == "END":
        break

    elif command == "green":
        while len(traffic_queue) > 0 and current_green > 0:
            ch = traffic_queue.popleft()

            if current_green > 0:
                total_cars_passed += 1
                current_green -= len(ch)

            if current_green < 0:
                current_free += current_green
                if current_free < 0:
                    idx = (-current_free)
                    car = ch
                    character_hit = car[-idx]
                    print(f"A crash happened!\n{car} was hit at {character_hit}.")
                    exit()

    else:
        traffic_queue.append(command)

if len(car) == 0:
    print(f"Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.")

