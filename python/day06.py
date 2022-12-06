from aocd import get_data
from dotenv import load_dotenv

load_dotenv()


def day06(message: str, n: int = 4) -> int:
    for i in range(n - 1, len(message)):
        if len(set(message[i-n:i])) == n:
            return i


if __name__ == '__main__':
    data = get_data(day=6, year=2022)
    print("Number of characters processed (part a):", day06(data))
    print("Number of characters processed (part b):", day06(data, n=14))


