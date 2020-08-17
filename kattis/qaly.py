import sys

n = int(sys.stdin.readline())

i = 0
while i < n:
    c = 0
    for line in sys.stdin:
        a = []
        for num in line:
            a.append(num)
            c += (a[0] * a[1])
            i += 1
