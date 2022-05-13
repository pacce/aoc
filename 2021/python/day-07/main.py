from argparse import ArgumentParser
import numpy as np


def gauss(n):
    return (n * (n + 1)) / 2


def first(ps):
    pmax    = np.max(ps)

    xs  = np.zeros(pmax)
    for i in range(pmax):
        consumption = np.abs(ps - i)
        xs[i]       = np.sum(consumption)
    best = np.argmin(xs)
    return int(xs[best])


def second(ps):
    pmax    = np.max(ps)

    xs  = np.zeros(pmax)
    for i in range(pmax):
        cs  = np.abs(ps - i)
        for c in cs:
            xs[i] += gauss(c)
    best = np.argmin(xs)
    return int(xs[best])



def main(args):
    ps  = np.loadtxt(args.file, delimiter=',', dtype=int)
    print('{}'.format(first(ps)))
    print('{}'.format(second(ps)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
