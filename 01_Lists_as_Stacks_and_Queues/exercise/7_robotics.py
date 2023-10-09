from collections import deque

robot_name = input().split(";")
time = [int(ch) for ch in input().split(":")]
free_robot = {}
working_robot = {}
el_for_work = deque()

for ch in robot_name:
    new_ch = ch.split("-")
    robot_name = new_ch[0]
    seconds = int(new_ch[1])
    free_robot[robot_name] = seconds

while True:
    elements = input()

    if elements == "End":
        break

    el_for_work.append(elements)

while el_for_work:
    current_element = el_for_work.popleft()
    time[2] += 1

    if time[2] == 60:
        time[1] += 1
        time[2] = 0
        if time[1] == 60:
            time[1] = 0
            time[0] += 1
            if time[0] == 24:
                time[0] = 0

    for i in working_robot:
        working_robot[i] += 1

    for key in free_robot:
        if key in working_robot:
            if working_robot[key] == free_robot[key]:
                del working_robot[key]

    if len(free_robot) != len(working_robot):
        for chart in free_robot:
            if chart not in working_robot:
                print(f"{chart} - {current_element} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
                working_robot[chart] = 0
                break
    else:
        el_for_work.append(current_element)

