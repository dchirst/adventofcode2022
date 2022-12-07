from dataclasses import dataclass

from aocd import get_data
from dotenv import load_dotenv

load_dotenv()


def get_dir_sizes(instructions):
    # initialise iterator of instructions
    inst = next(instructions)
    dir_sizes = []

    total_size = 0

    # Get file sizes inside directory
    if inst.startswith("$ ls"):
        while inst := next(instructions, None):
            # count all file sizes towards total size
            if inst.split()[0].isnumeric():
                total_size += int(inst.split()[0])
            elif inst.startswith("dir"):
                continue
            # if next instruction is a new command (denoted by $), then the ls command is over so break the loop
            elif inst.startswith("$"):
                break
            else:
                raise Exception(f"Unknown line {inst}")

    # iterate through all folders in current directory
    while True:
        # if stepping out, you're finished with the directory
        if not inst or inst.startswith("$ cd .."):
            dir_sizes.append(total_size)
            return total_size, dir_sizes, instructions
        # if stepping in, use recursion to find size of subdirectory
        elif inst.startswith("$ cd"):
            sub_dir_size, sub_dir_sizes, instructions = get_dir_sizes(instructions)
            dir_sizes += sub_dir_sizes
            total_size += sub_dir_size
            inst = next(instructions, None)

        else:
            raise Exception(f"Unknown line {inst}")


def day07(data: str, max_dir_size: int = 1e5, disk_space: int = 7e7, space_needed: int = 3e7):
    instructions = iter(data.split("\n"))
    next(instructions)
    total_size, dir_sizes, _ = get_dir_sizes(instructions)
    return sum([d for d in dir_sizes if d <= max_dir_size]), \
           min([x for x in dir_sizes if x >= space_needed - (disk_space - max(dir_sizes))])


if __name__ == '__main__':
    data = get_data(day=7, year=2022)

    suitable_dir_total, smallest_suitable_dir_size= day07(data)

    print("Size of all sub-100_000 directories (part a):", suitable_dir_total)
    print("Size of smallest dir over 30 million (part b)", smallest_suitable_dir_size)
