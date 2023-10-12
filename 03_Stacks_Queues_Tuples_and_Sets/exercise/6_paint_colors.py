from collections import deque

secondary_dict = {"orange": ["red", "yellow"], "purple": ["red", "blue"], "green": ["yellow", "blue"]}
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
matched_main = []
str_list = deque([ch for ch in input().split(" ")])

while len(str_list) > 0:
    current_str = ''
    reversed_current_str = ''

    if len(str_list) > 1:
        part_one = str_list.popleft()
        part_two = str_list.pop()
        current_str = part_one + part_two
        reversed_current_str = part_two + part_one

        if current_str in main_colors:
            matched_main.append(current_str)
            continue
        elif current_str in secondary_colors:
            matched_main.append(current_str)
            continue
        elif reversed_current_str in main_colors:
            matched_main.append(reversed_current_str)
        elif reversed_current_str in secondary_colors:
            matched_main.append(reversed_current_str)
        else:
            current_one = part_one[:-1]
            current_two = part_two[:-1]

            if len(str_list) > 1:
                index = len(str_list) // 2

                if current_two != "":
                    str_list.insert(index, current_two)

                if current_one != "":
                    str_list.insert(index, current_one)

            elif len(str_list) <= 1:

                if current_two != "":
                    str_list.appendleft(current_two)

                if current_one != "":
                    str_list.appendleft(current_one)

    else:
        part_one = str_list.popleft()
        current_str = part_one

        if current_str in main_colors:
            matched_main.append(current_str)
            continue
        elif current_str in secondary_colors:
            matched_main.append(current_str)
            continue
        else:
            current_one = part_one[:-1]

            if current_one != "":
                str_list.append(current_one)

final_list = []

for ch in matched_main:
    count = 0

    if ch in secondary_colors:
        for key in secondary_dict[ch]:
            if key in matched_main:
                count += 1
    else:
        final_list.append(ch)

    if count == 2:
        final_list.append(ch)

print(final_list)

