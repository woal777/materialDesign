import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', help='The num you wish to calc', type=int)

    args = parser.parse_args()

    result = fib(args.num)
    print("The " + args.num.__str__() + 'th fib number is ' + result.__str__())


if __name__ == '__main__':
    run()
