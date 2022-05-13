from argparse import ArgumentParser
import numpy as np


NEWBORN = 8


class School(object):
    def __init__(self, fishes):
        self.days = [0] * (NEWBORN + 1)
        for fish in fishes:
            self.days[int(fish)] += 1
        self.i = 0

    def __str__(self):
        return '{}'.format(self.days)

    def __repr__(self):
        return str(self)

    def count(self):
        return sum(self.days)

    def update(self):
        today = self.i % len(self.days)
        self.days[(today + 7) % len(self.days)] += self.days[today]

        self.i += 1



def main(args):
    school = School(np.loadtxt(args.file, delimiter=','))
    for _ in range(256):
        school.update()
    print(school.count())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
