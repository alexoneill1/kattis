import sys

def main():
    a = []
    for line in sys.stdin:
        line = line.strip()
        a.append(line)
    if a[0] > a[1]:
        print('no')
    else:
        print('go')

if __name__ == "__main__":
    main()
