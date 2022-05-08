from argparse import ArgumentParser
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


WINDOW = 3


def main(args):
    xs = np.loadtxt(args.file)  # Loads dataset
    ys = np.diff(xs)            # Evaluates difference with previous value, removing boundaries

    # Solves part 1
    ys[ys < 0] = 0
    ys[ys > 0] = 1
    print(np.sum(ys, dtype=int))

    ws = sliding_window_view(xs, WINDOW)    # Generates rolling window
    ss = np.sum(ws, axis=1)                 # Sums each rolling window entry
    ys = np.diff(ss)                        # Evaluates difference with previous value, removing boundaries

    # Solves part 2
    ys[ys < 0] = 0
    ys[ys > 0] = 1
    print(np.sum(ys, dtype=int))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
