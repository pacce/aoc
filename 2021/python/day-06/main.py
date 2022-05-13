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

    def simulate(self, days):
        for _ in range(days):
            self.update()
        return self.count()



def main(args):
    fishes  = np.loadtxt(args.file, delimiter=',')
    first   = School(fishes)
    second  = School(fishes)
    # First day
    print(first.simulate(80))
    # Second day
    print(second.simulate(256))



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
