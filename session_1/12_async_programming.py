import asyncio
import random


async def slow_add(a, b):
    await asyncio.sleep(0.5)
    return a+b


async def main():
    for _ in range(10):
        a = random.randint(0, 20)
        b = random.randint(0, 50)
        print(f"{a}+{b}={await slow_add(a, b)}")


if __name__ == "__main__":
    asyncio.run(main())
