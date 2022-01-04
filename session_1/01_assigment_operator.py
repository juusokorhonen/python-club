import os


def f(a, b, /, c):
    print(f"{a=}, {b=}, {c=}")


def operate(a, b, /, *, operator='+'):
    if operator == '+':
        print(f"{a+b=}")
    if operator == '-':
        print(f"{a-b=}")
    if operator == '*':
        print(f"{a*b=}")
    if operator == '/':
        print(f"{a/b=}")
    if operator == '**':
        print(f"{a**b=}")


def main():
    # Old way
    if len(os.environ.keys()) > 30:
        print("There are >30 keys in os.environ.")
        print(f"There are {len(os.environ.keys())} keys to be exact.")

    # New in 3.8
    if (n := len(os.environ.keys())) > 30:
        print("There are >30 keys in os.environ.")
        print(f"There are {n} keys to be exact.")

    while (n := input('input number: ')) != "":
        print(n)

    n = input('input number: ')
    while n != "":
        print(n)
        n = input('input number: ')

    # Positional-only parameters
    f(1, 2, 3)   # ok
    f(1, 2, c=3)   # ok
    try:
        f(a=1, b=2, c=3)
    except TypeError as e:
        print(e)

    try:
        f(1, b=2, c=3)
    except TypeError as e:
        print(e)

    # Keyword-only parameters
    operate(1, 2)
    operate(1, 2, operator='*')
    operate(1, 2, operator='/')

    try:
        operate(1, 2, '-')
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
