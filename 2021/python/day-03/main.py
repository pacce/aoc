from argparse import ArgumentParser
import numpy as np


def condition(line):
    return np.array([int(c) for c in line])


def gamma(xs):
    ss      = np.sum(xs, axis=0)
    length  = int(xs.shape[0] / 2.0)
    binary  = reversed([1 if s > length else 0 for s in ss])

    sum = 0
    for (i, b) in enumerate(binary):
        sum += (b * (2 ** i))
    return sum


def epsilon(xs):
    ss      = np.sum(xs, axis=0)
    length  = int(xs.shape[0] / 2.0)
    binary  = reversed([0 if s > length else 1 for s in ss])

    sum = 0
    for (i, b) in enumerate(binary):
        sum += (b * (2 ** i))
    return sum


def fst(xs):
    return gamma(xs) * epsilon(xs)


def main(args):
    with open(args.file, 'r') as fd:
        lines = [x.split()[0] for x in fd.readlines()]
    xs = np.stack([condition(line) for line in lines])
    print(fst(xs))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
