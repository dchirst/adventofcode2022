from aocd import get_data
from dotenv import load_dotenv

load_dotenv()


def find_common_item_one(contents: str) -> str:
    split_point = len(contents) // 2
    compartment1, compartment2 = contents[:split_point], contents[split_point:]
    return next(iter(set(compartment1).intersection(set(compartment2))))


def find_common_item_three(contents: list[str]) -> str:
    print(contents)
    return next(iter(set(contents[0]).intersection(set(contents[1]), set(contents[2]))))


def priority(char: str) -> int:
    num = ord(char)
    return num - 96 if num > 90 else num - 38


def day03_a(all_contents: str) -> int:
    return sum(map(lambda x: priority(find_common_item_one(x)), all_contents.split("\n")))


def day03_b(all_contents: str) -> int:
    rucksack_contents = all_contents.split("\n")
    return sum(map(lambda x: priority(find_common_item_three(rucksack_contents[x:x + 3])),
                   range(0, len(rucksack_contents), 3)))


if __name__ == '__main__':
    data = get_data(session, day=3, year=2022)
    print(day03_a(data))
    print(day03_b(data))
