from argparse import ArgumentParser
# import numpy as np


class Accumulator(object):
    def __init__(self, length):
        self.acc    = [0] * length
        self.count  = 0

    def update(self, line):
        self.count += 1
        for (i, c) in enumerate(line):
            self.acc[i] += int(c)

    def msb(self):
        count = int(self.count / 2)
        return [
                1
                if x > count else 0
                for x in self.acc
                ]

    def lsb(self):
        count = int(self.count / 2)
        return [
                0
                if x > count else 1
                for x in self.acc
                ]

    def gamma(self):
        acc = 0
        vs  = self.msb()
        vs.reverse()
        for (i, v) in enumerate(vs):
            acc += (v * (2 ** i))
        return acc

    def epsilon(self):
        acc = 0
        vs  = self.lsb()
        vs.reverse()
        for (i, v) in enumerate(vs):
            acc += (v * (2 ** i))
        return acc

    def fst(self):
        return self.gamma() * self.epsilon()


def main(args):
    with open(args.file, 'r') as fd:
        lines = [x.split()[0] for x in fd.readlines()]

    accumulator = Accumulator(len(lines[0]))
    for line in lines:
        accumulator.update(line)
    print(accumulator.fst())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
