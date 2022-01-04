from typing import Union


def square_39(number: Union[int, float]) -> Union[int, float]:
    return number ** 2


def square_310(number: int | float) -> int | float:
    # PEP604
    return number ** 2


def main():
    # Python >=3.9
    x: list[int] = []
    y = list[int]()
    # Python <3.9
    #z = List[int] = []

    numbers = [3, 3.3, 3.14159265358]
    for number in numbers:
        assert isinstance(number, int | float)

        out39 = square_39(number)
        print(out39)
        out310 = square_310(number)
        print(out310)
        assert out39 == out310


if __name__ == "__main__":
    main()
