import re

from aocd import get_data
from dotenv import load_dotenv

load_dotenv()


def parse_initial_stack(stack: str) -> dict:
    lines = stack.split("\n")
    cols = lines[-1].split()
    stacks = {k: [] for k in cols}
    for line in lines[:-1]:
        for i, idx in enumerate(range(1, len(line), 4)):
            if not line[idx].isspace():
                stacks[cols[i]].append(line[idx])
    return stacks


def parse_data(d: str) -> tuple:
    initial_stack, procedure = d.split("\n\n")
    stack = parse_initial_stack(initial_stack)
    procedure = re.findall("move (\d+) from (\d+) to (\d+)", procedure)
    return stack, procedure


def day05_a(data: str) -> str:
    stack, procedure = parse_data(data)
    for num, from_idx, to_idx in procedure:
        for _ in range(int(num)):
            stack[to_idx].insert(0, stack[from_idx].pop(0))

    return "".join(s[0] for s in stack.values())


def day05_b(data: str)  -> str:
    stack, procedure = parse_data(data)
    for num, from_idx, to_idx in procedure:
            stack[to_idx] = stack[from_idx][:int(num)] + stack[to_idx]
            stack[from_idx] = stack[from_idx][int(num):]

    return "".join(s[0] for s in stack.values())


if __name__ == '__main__':
    data = get_data(year=2022, day=5)
    print(day05_a(data))
    print(day05_b(data))