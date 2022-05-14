from argparse import ArgumentParser
import numpy as np


def condition(line):
    return np.array([int(c) for c in line])


def decimal(xs):
    sum = 0
    for (i, x) in enumerate(reversed(xs)):
        sum += (x * (2 ** i))
    return sum


def gamma(xs):
    ss      = np.sum(xs, axis=0)
    length  = int(xs.shape[0] / 2.0)
    binary  = [1 if s > length else 0 for s in ss]

    return decimal(binary)


def epsilon(xs):
    ss      = np.sum(xs, axis=0)
    length  = int(xs.shape[0] / 2.0)
    binary  = [0 if s > length else 1 for s in ss]

    return decimal(binary)


def oxygen(xs, index=0):
    x = xs[:, index]

    ss      = np.sum(xs, axis=0)
    length  = xs.shape[0] / 2.0

    bit         = int(ss[index] >= length)
    location    = np.where(x == bit)[0]
    xs          = xs[location]

    if xs.shape[0] == 1:
        return decimal(xs.ravel())
    else:
        return oxygen(xs, index + 1)


def carbon(xs, index=0):
    x = xs[:, index]

    ss      = np.sum(xs, axis=0)
    length  = xs.shape[0] / 2.0

    bit         = int(ss[index] < length)
    location    = np.where(x == bit)[0]
    xs          = xs[location]

    if xs.shape[0] == 1:
        return decimal(xs.ravel())
    else:
        return carbon(xs, index + 1)


def fst(xs):
    return gamma(xs) * epsilon(xs)


def snd(xs):
    return oxygen(xs) * carbon(xs)


def main(args):
    with open(args.file, 'r') as fd:
        lines = [x.split()[0] for x in fd.readlines()]
    xs = np.stack([condition(line) for line in lines])
    print(fst(xs))
    print(snd(xs))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
