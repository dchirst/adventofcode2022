from itertools import product, starmap

import numpy as np
from dotenv import load_dotenv

load_dotenv()


def visible_outside_one_direction(arr: np.ndarray, reverse=False) -> np.ndarray:
    # Get the maximum tree height from previous trees
    maxes = np.maximum.accumulate(
            arr[::-1] if reverse else arr)[:-1]
    # the first tree does not have any previous tree, so set it to -1 so first tree will always get picked up
    maxes = np.insert(maxes, 0, -1)
    # compare tree height to maximum previous tree height - it's visible if the tree is taller than previous max
    return arr > (maxes[::-1] if reverse else maxes)


def day08_a(data: np.ndarray) -> int:
    return int(
        # Count number of trees with clear sight lines
        np.sum(
            # A tree is visible if it is visible rom any direction
            np.any(
                np.stack(
                    # Iterate through directions (left, right, top, bottom), seeing which trees are visible from each direction
                    starmap(lambda ax, rev:
                            # iterate through rows of trees, finding which ones are visible from a given direction
                            np.apply_along_axis(visible_outside_one_direction, ax, data, reverse=rev),
                            product((0, 1), (False, True)))),
                axis=0
            )
        )
    )


def scenic_score(arr: np.ndarray, reverse=False) -> np.array:
    # if reversed (i.e. from right direction not left), reverse array
    a = arr[::-1] if reverse else arr
    scores = np.append(
        np.fromiter(
            # iterate through each tree
            map(lambda i:
                # Find first index after current tree where tree is bigger than current tree
                # if there are no subsequent trees bigger than current tree, return total number of trees left
                np.argmax(a[i + 1:] >= a[i]) + 1 if np.any(a[i + 1:] >= a[i]) else len(arr) - 1 - i,
                range(len(arr) - 1)),
            dtype=np.int),
        0)
    return scores[::-1] if reverse else scores


def day08_b(data: np.ndarray) -> int:
    # return maximum scenic score
    return np.max(
        # score is the product of scenic score from all directions
        np.prod(np.stack(
                    # iterate through directions
                    starmap(lambda ax, rev:
                            # iterate through rows of trees, finding scenic score for a given direction
                            np.apply_along_axis(scenic_score, ax, data, reverse=rev),
                            product((0, 1), (False, True)))
                ), axis=0))


if __name__ == '__main__':
    arr = np.genfromtxt("../inputs/day08.txt", delimiter=1, dtype=int)
    print("Number of visible trees (part a):", day08_a(arr))
    print("Maximum scenic score (part b):", day08_b(arr))

