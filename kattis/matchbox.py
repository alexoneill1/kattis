n = input()
N = input().readline()

n, w, h = n.split()

sides = (int(w) ** 2) + (int(h) ** 2)

i = 0
while i < int(n):
    if (int(input() > int(sides))):
        print('DA')
    else:
        print('NE')
    i += 1
