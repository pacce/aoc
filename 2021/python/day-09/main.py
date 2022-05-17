from argparse import ArgumentParser
from functools import reduce
import itertools
import numpy as np


HILL = 9


def condition(line):
    line = line.strip()
    cs = np.array([int(c) for c in line])
    return cs


def extremes(c, pmax):
    cx, cy      = c
    xmax, ymax  = pmax
    return (cx >= 0 and cx < xmax) and (cy >= 0 and cy < ymax)


def neighbour(p, pmax):
    x, y    = p
    cs      = [(x - 1, y + 0), (x + 1, y + 0), (x + 0, y - 1), (x + 0, y + 1)]

    return list(filter(lambda c: extremes(c, pmax), cs))


def flows(zs, p, pmax):
    return {c for c in neighbour(p, pmax) if zs[c] != HILL}


def basin(zs, ps, p, pmax):
    fs = flows(zs, p, pmax)

    intersection    = ps & fs
    unexplored      = intersection ^ fs

    ps.update(fs)

    if len(unexplored) == 0:
        return {}

    for f in fs:
        ps.update(basin(zs, ps, f, pmax))
    return ps


def valley(zs, p, pmax):
    ps = {p}
    return basin(zs, ps, p, pmax)


def first(zs):
    xmax, ymax  = zs.shape
    pmax        = (xmax, ymax)

    depth = []
    for p in itertools.product(range(xmax), range(ymax)):
        v   = zs[p]
        vs  = [zs[c] for c in neighbour(p, pmax)]
        if v < min(vs):
            depth.append(v + 1)
    return np.sum(depth)


def second(zs):
    xmax, ymax  = zs.shape
    pmax        = (xmax, ymax)

    bs = []
    for p in itertools.product(range(xmax), range(ymax)):
        v   = zs[p]
        vs  = [zs[c] for c in neighbour(p, pmax)]
        if v < min(vs):
            b = valley(zs, p, pmax)
            bs.append(len(b))

    bs = sorted(bs)

    return reduce((lambda x, y: x * y), bs[-3:])


def main(args):
    with open(args.file, 'r') as fd:
        zs = np.stack([condition(line) for line in fd.readlines()])
    print('First    : {}'.format(first(zs)))
    print('Second   : {}'.format(second(zs)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
