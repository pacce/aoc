from argparse import ArgumentParser
import itertools
import numpy as np



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


def main(args):
    with open(args.file, 'r') as fd:
        zs = np.stack([condition(line) for line in fd.readlines()])
    print('First: {}'.format(first(zs)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
