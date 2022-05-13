from argparse import ArgumentParser
import numpy as np


NEWBORN = 8
REBIRTH = 6


class Fish(object):
    def __init__(self, age):
        self.age = age

    @classmethod
    def birth(cls):
        return cls(NEWBORN)

    def __str__(self):
        return '{:.0f}'.format(self.age)

    def __repr__(self):
        return str(self)

    def step(self):
        if self.age == 0:
            self.age = REBIRTH
        else:
            self.age -= 1

    def update(self):
        newborn = None
        if self.age == 0:
            newborn = Fish.birth()
        self.step()
        return newborn


class School(object):
    def __init__(self, fishes):
        self.fishes = fishes

    def __str__(self):
        return '{}'.format(self.fishes)

    def __repr__(self):
        return str(self)

    def update(self):
        fishes = self.fishes[:]
        for fish in self.fishes:
            if (newborn := fish.update()) is not None:
                fishes.append(newborn)
            else:
                pass
        self.fishes = fishes

    def count(self):
        return len(self.fishes)


def main(args):
    school = School([Fish(x) for x in np.loadtxt(args.file, delimiter=',')])
    for _ in range(80):
        school.update()
    print(school.count())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
