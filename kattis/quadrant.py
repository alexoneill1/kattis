import sys

def main():
    a = []
    for line in sys.stdin:
        a.append(int(line))
    if a[0] > 0:
        if a[1] > 0:
            print('1')
        else:
            print('4')
    elif a[0] < 0:
        if a[1] > 0:
            print('2')
        else: 
            print('3')

if __name__ == "__main__":
    main()