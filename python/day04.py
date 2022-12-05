from aocd import get_data
from dotenv import load_dotenv

load_dotenv()


def contains(pair: str) -> bool:
    elf1, elf2 = pair.split(",")
    elf1_start, elf1_stop = tuple(map(int, elf1.split("-")))
    elf2_start, elf2_stop = tuple(map(int, elf2.split("-")))
    return (elf1_start <= elf2_start and elf1_stop >= elf2_stop) or (
                elf1_start >= elf2_start and elf1_stop <= elf2_stop)


def overlaps(pair: str) -> bool:
    elf1, elf2 = pair.split(",")
    elf1_start, elf1_stop = tuple(map(int, elf1.split("-")))
    elf2_start, elf2_stop = tuple(map(int, elf2.split("-")))
    return (elf1_start <= elf2_start <= elf1_stop) or (elf1_start <= elf2_stop <= elf1_stop) or \
           (elf1_start >= elf2_start and elf1_stop <= elf2_stop)


def day04_a(cleaning_pairs: str) -> int:
    return sum(map(contains, cleaning_pairs.split("\n")))


def day04_b(cleaning_pairs: str) -> int:
    return sum(map(overlaps, cleaning_pairs.split("\n")))


if __name__ == '__main__':
    with open("../inputs/day04_test.txt", "r") as f:
        test_data = f.read()
        print(day04_a(test_data))
        print(day04_b(test_data))

    data = get_data(day=4, year=2022)
    print(day04_a(data))
    print(day04_b(data))
