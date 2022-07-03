"""
Simulate 'The 100 Prisoners Problem'.
Came across this intersting problem from,
Veritasium's video : https://www.youtube.com/watch?v=iSNsgj1OCLA
Wiki : https://en.wikipedia.org/wiki/100_prisoners_problem
"""
from argparse import ArgumentParser
import numpy as np


def each_prisoner(prisoner):
    """
    Each prisoner gets N_CHANCES,
    if any prisoner fails all prisoners are killed.
    """

    found_val = boxes[prisoner-1]

    for _ in range(N_CHANCES):
        if found_val == prisoner:
            return True
        found_val = boxes[found_val-1]

    return False


def each_experiment():
    """Run whole experiment once."""

    # boxes are labled with index+1 (1...N)
    # containing the values at index+1 inside them
    global boxes
    boxes = np.random.permutation(np.arange(1, N_PRISONERS+1))

    # prisoners are randomly picked
    prisoners = np.random.permutation(np.arange(1, N_PRISONERS+1))

    return all(map(each_prisoner, prisoners))


if __name__ == "__main__":
    parser = ArgumentParser(description='Simulate the 100 prisoners problem.')
    parser.add_argument('-N', type=int, nargs='?', default=1000, help='no. of times the experiment has to be performed')
    parser.add_argument('-n', type=int, nargs='?', default=100, help='no. of prisoners')
    args = parser.parse_args()

    n_simul = args.N
    N_PRISONERS = args.n
    N_CHANCES = N_PRISONERS//2

    print(f"Simulating {n_simul} times, with {N_PRISONERS} prisoners:")
    n_success = sum(each_experiment() for _ in range(n_simul))
    prob_success = n_success/n_simul
    print(f"{prob_success}")
