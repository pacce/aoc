from argparse import ArgumentParser
import numpy as np


def numbers(line):
    line = line.split(',')
    return [int(c) for c in line]


def condition(lines):
    header  = numbers(lines[0])
    lines   = lines[1:]

    count  = int(len(lines) / 6)

    boards = []
    for _ in range(count):
        current, lines = lines[1:6], lines[6:]
        boards.append(Board(current))

    return header, boards


def board(lines):
    return np.stack([
        np.array([int(c) for c in line.split()])
        for line in lines
        ])


class Board(object):
    def __init__(self, lines):
        self.xs = board(lines)
        self.mask = np.full(self.xs.shape, False)

    def __str__(self):
        return '{}'.format(self.xs)

    def update(self, value):
        index = np.where(self.xs == value)
        self.mask[index] = True

    def row_check(self):
        rs = np.all(self.mask, axis=1)
        return np.any(rs)

    def col_check(self):
        rs = np.all(self.mask, axis=0)
        return np.any(rs)

    def check(self):
        return self.col_check() or self.row_check()

    def coalesce(self, value):
        if self.check() is False:
            raise ValueError('board is not complete')
        unmarked = self.xs[np.logical_not(self.mask)]
        return np.sum(unmarked) * value

def fst(values, bs):
    for value in values:
        for (i, b) in enumerate(bs):
            b.update(value)
            if b.check():
                return b.coalesce(value)


def main(args):
    with open(args.file, 'r') as fd:
        lines = [x.strip() for x in fd.readlines()]
    values, bs = condition(lines)
    print(fst(values, bs))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
