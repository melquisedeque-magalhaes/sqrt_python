import datetime
import math


def computer(end, start=1):
    pos = start
    while pos < end:
        pos += 1
        math.sqrt((pos - 1000000) * (pos - 1000000))


def main():
    start = datetime.datetime.now()
    end = 50000000
    computer(end)
    time = datetime.datetime.now() - start
    print(f"Terminou em {time.total_seconds():.2f} segundos")


if __name__ == '__main__':
    main()
