from argparse import ArgumentParser
import itertools
import numpy as np


def condition(line):
    fst, snd = line.split(' -> ')

    fst = [int(c) for c in fst.split(',')]
    snd = [int(c) for c in snd.split(',')]

    return (fst, snd)


def vertical(x, ys):
    ymin, ymax  = np.min(ys), np.max(ys)
    ys          = list(range(ymin, ymax + 1))
    return list(itertools.product([x], ys))


def horizontal(xs, y):
    xmin, xmax  = np.min(xs), np.max(xs)
    xs          = list(range(xmin, xmax + 1))
    return list(itertools.product(xs, [y]))


class Board(object):
    def __init__(self, x, y):
        self.xs = np.zeros((x + 1, y + 1))

    def __str__(self):
        return '{}'.format(self.xs)

    def update(self, c):
        fst, snd = c

        if fst[0] == snd[0]:
            ps = vertical(fst[0], [fst[1], snd[1]])

            for (x, y) in ps:
                self.xs[x, y] += 1

        if fst[1] == snd[1]:
            ps = horizontal([fst[0], snd[0]], fst[1])

            for (x, y) in ps:
                self.xs[x, y] += 1

    def count(self):
        return len(np.where(self.xs >= 2)[0])


def fst(cs):
    x, y = 0, 0
    for c in cs:
        fst, snd = c
        x, y = max(x, fst[0], snd[0]), max(y, fst[1], snd[1])

    b = Board(x, y)
    for c in cs:
        b.update(c)

    return b.count()



def main(args):
    with open(args.file, 'r') as fd:
        lines = [x.strip() for x in fd.readlines()]
    cs = [condition(line) for line in lines]
    print(fst(cs))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
