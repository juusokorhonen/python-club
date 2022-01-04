import random
import secrets
import time


def main():
    # Non-cryptographical random bytes
    random_data = random.randbytes(80)
    print(random_data)

    # Cryptographical random bytes
    random_data_2 = secrets.token_bytes(80)
    print(random_data_2)

    t_start = time.perf_counter()
    for i in range(1000000):
        random.randbytes(80)
    t_random = time.perf_counter() - t_start
    print(f"random.randbytes(80): {t_random} s")

    t_start = time.perf_counter()
    for i in range(1000000):
        secrets.token_bytes(80)
    t_secrets = time.perf_counter() - t_start
    print(f"secrets.token_bytes(80): {t_secrets} s")


if __name__ == "__main__":
    main()
