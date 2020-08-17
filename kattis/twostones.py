import sys

def main():
    for num in sys.stdin:
        if int(num) % 2 == 1:
            print('Alice')
        else:
            print('Bob')

if __name__ == "__main__":
    main()
