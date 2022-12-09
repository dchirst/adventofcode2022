import operator
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()


def knot_too_far(head, tail) -> bool:
    return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1


def new_knot_pos(head, tail) -> bool:
    for ax in (0, 1):
        if head[ax] > tail[ax]:
            tail[ax] += 1
        elif head[ax] < tail[ax]:
            tail[ax] -= 1

    return tail


def move_head(direction, pos) -> tuple:
    match direction:
        case "R":
            y_axis = False
            op = operator.add
        case "L":
            y_axis = False
            op = operator.sub
        case "U":
            y_axis = True
            op = operator.add
        case "D":
            y_axis = True
            op = operator.sub
        case _:
            raise Exception(f"Unknown direction: {direction}")

    ax = int(y_axis)
    pos[ax] = op(pos[ax], 1)

    return pos


def move_knot(head, tail) -> tuple:
    if knot_too_far(head, tail):
        tail = new_knot_pos(head, tail)
    return tail


def day09(data: str, num_knots: int = 10) -> int:
    tail_pos = set()
    knots = [[0, 0] for _ in range(num_knots)]
    # iterate through instructions
    for inst in data.split("\n"):
        direction, amount = inst.split()
        # iterate through amount of movements
        for _ in range(int(amount)):

            knots[0] = move_head(direction, knots[0])

            for i in range(1, num_knots):
                knots[i] = move_knot(knots[i-1], knots[i])

            tail_pos.add(tuple(knots[-1]))

    return len(tail_pos)


if __name__ == '__main__':
    data = get_data(day=9, year=2022)

    print("Number of positions tail visits (part a):", day09(data, num_knots=2))
    print("Number of positions tail visits (part b):", day09(data, num_knots=10))

