balance_list = []
parentheses = input()
pairs = ["{}", "()", "[]"]

for el in parentheses:
    if el == "{" or el == "(" or el == "[":
        balance_list.append(el)
    else:
        if len(balance_list) > 0:
            opposite_ch = balance_list.pop()
            new_string = opposite_ch + el
            if new_string in pairs:
                continue
            else:
                print("NO")
                exit()
        else:
            print("NO")
            exit()

if len(balance_list) == 0:
    print("YES")

