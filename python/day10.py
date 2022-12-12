from aocd import get_data
from dotenv import load_dotenv

load_dotenv()


def day10_a(data: str, cycles: tuple[int]) -> int:
    cycle = signal_strengths = i = 0
    x = 1
    cycles_to_monitor = iter(cycles)
    next_cycle_to_monitor = next(cycles_to_monitor)
    for inst in data.split("\n"):
        match inst.split():
            case ["noop"]:
                cycles_to_add = 1
                x_to_add = 0
            case "addx", amt:
                cycles_to_add = 2
                x_to_add = int(amt)
            case _:
                raise Exception(f"Unknown command {inst}")

        for _ in range(cycles_to_add):
            print("#", end="") if abs(x - i) <= 1 else print(".", end="")
            i += 1
            if (i % 40 == 0):
                print()
                i = 0

        if cycle + cycles_to_add >= next_cycle_to_monitor:
            signal_strengths += next_cycle_to_monitor * x
            try:
                next_cycle_to_monitor = next(cycles_to_monitor)
            except StopIteration:
                return signal_strengths

        cycle += cycles_to_add
        x += x_to_add

    return signal_strengths

if __name__ == '__main__':

    data = get_data(day=10, year=2022)

    cycles = (20, 60, 100, 140, 180, 220)

    print("\nSignal strength:", day10_a(data, cycles))

