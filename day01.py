from timeit import default_timer as timer


def day1_a(data: str) -> int:
    """
    First draft answer, using a single for loop

    :param data: Data from advent of code input, read from file as string
    :return: Maximum number of calories for an elf
    """
    max_cal = 0
    current_cal = 0
    for cal in data.split("\n"):
        if cal.isnumeric():
            current_cal += int(cal)
        else:
            if current_cal > max_cal:
                max_cal = current_cal
            current_cal = 0
    return max_cal


def day1_a_one_line(data: str) -> int:
    """
    Trying to put first answer all in one line. Still runs faster than day1_a (I think because of the map function)

    :param data: Data from advent of code input, read from file as string
    :return: Maximum number of calories for an elf
    """
    return max(map(sum, map(lambda x: map(int, x), map(lambda x: x.split("\n"), data.split("\n\n")))))


def day1_b(data: str) -> int:
    """
    First draft day 1 b answer.

    :param data: Data from advent of code input, read from file as string
    :return: Maximum number of calories for top 3 elves
    """
    top_3_cals = [0, 0, 0]
    current_cal = 0
    for cal in data.split("\n"):
        if cal.isnumeric():
            current_cal += int(cal)
        else:
            if current_cal > top_3_cals[0]:
                top_3_cals[0] = current_cal
                top_3_cals.sort()
            current_cal = 0

    return sum(top_3_cals)


if __name__ == '__main__':
    with open("inputs/day1.txt", "r") as f:
        data = f.read()
        for fn in (day1_a, day1_a_one_line, day1_b):
            times = []
            answers = []
            for _ in range(5):
                start = timer()
                ans = fn(data)
                end = timer()
                times.append(end - start)
                answers.append(ans)
            assert all(x == answers[0] for x in answers)
            print("Answer:", answers[0])
            print(f"Average time for {fn.__name__}:", (sum(times) / len(times)) * 1e6, "µs")
