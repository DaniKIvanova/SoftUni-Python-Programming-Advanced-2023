def fill_list(count):
    list = []
    for _ in range(count):
        list.append(input())
    return list


n = int(input())
usernames = fill_list(n)

for name in set(usernames):
    print(name)

    