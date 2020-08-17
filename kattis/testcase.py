import sys

def get_odds():

    lst = []
    num = input()
    while num != "-1":
        if int(num) % 2 != 0:
            lst.append(int(num)
        num = input()
    return lst
print(get_odds())