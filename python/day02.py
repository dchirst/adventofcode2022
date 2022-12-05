from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

MOVE_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


def win_loss_draw(opp, you):
    result_num = ord(you) - ord(opp) - 23
    if result_num == 0:
        result = 3
    elif result_num in (-1, 2):
        result = 0
    else:
        result = 6

    return result


def move_from_result(opp, result):
    opp_num = ord(opp)
    if result == 3:
        you_num = opp_num
    elif result == 0:
        you_num = opp_num + 2 if opp_num - 65 == 0 else opp_num - 1

    else:
        you_num = opp_num - 2 if opp_num - 65 == 2 else opp_num + 1

    return chr(you_num + 23)


def score(wld, your_move):
    return wld + MOVE_SCORE[your_move]


def day02_a(data):
    total_score = 0
    for idx, round in enumerate(data.split("\n")):
        opponent, you = round.split(" ")
        result = win_loss_draw(opponent, you)
        total_score += score(result, you)

    return total_score


def day02_b(data):
    total_score = 0
    for r in data.split("\n"):
        opponent, result = r.split(" ")
        result = (ord(result) - 88) * 3
        you = move_from_result(opponent, result)
        total_score += score(result, you)

    return total_score


if __name__ == '__main__':
    data = get_data(session, day=2, year=2022)
    print(day02_a(data))
    print(day02_b(data))
