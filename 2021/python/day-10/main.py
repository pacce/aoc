from argparse import ArgumentParser
from functools import reduce


CORRUPTED = { ')': 3
            , ']': 57
            , '}': 1197
            , '>': 25137
            }

FIX = { '(': 1
      , '[': 2
      , '{': 3
      , '<': 4
      }


class Chunk(object):
    def __init__(self, left=None, right=None):
        self.left   = left
        self.right  = right

    def corrupted(self):
        if self.incomplete():
            return False
        elif self.left == '(' and self.right == ')':
            return False
        elif self.left == '[' and self.right == ']':
            return False
        elif self.left == '{' and self.right == '}':
            return False
        elif self.left == '<' and self.right == '>':
            return False
        else:
            return True

    def update(self, right):
        if self.incomplete():
            self.right = right
            return True
        else:
            return False

    def incomplete(self):
        return self.left is None or self.right is None

    def __str__(self):
        return '{}{}'.format(self.left, self.right)

    def __repr__(self):
        left    = ''
        right   = ''

        if self.left:
            left = self.left
        if self.right:
            right = self.right

        return '{}{}'.format(left, right)


def left(c):
    return c == '(' or c == '[' or c == '{' or c == '<'


def right(c):
    return c == ')' or c == ']' or c == '}' or c == '>'


def search(cs, el):
    for (i, c) in enumerate(reversed(cs)):
        if c.update(el):
            return i


def process(line):
    cs      = []
    for el in line:
        if left(el):
            cs.append(Chunk(el))
        elif right(el):
            index = search(cs, el)
            if cs[index].corrupted():
                return cs
        else:
            raise ValueError('unexpected char')
    return cs


def corrupted(cs):
    for c in cs:
        if c.corrupted():
            return True
    return False


def error(cs):
    for c in cs:
        if c.corrupted():
            return CORRUPTED[c.right]
    raise ValueError('no error detected')


def fix(cs):
    accumulator = 0
    for c in reversed(cs):
        if c.incomplete():
            accumulator *= 5
            accumulator += FIX[c.left]
    return accumulator

def first(lines):
    cs = [process(line) for line in lines]
    cs = filter(lambda c : corrupted(c), cs)
    es = [error(c) for c in cs]
    return reduce(lambda x, y: x + y, es)


def second(lines):
    cs = [process(line) for line in lines]
    cs = filter(lambda c: not corrupted(c), cs)
    es = sorted([fix(c) for c in cs])

    return es[int(len(es) / 2)]


def main(args):
    with open(args.file, 'r') as fd:
        lines = [line.strip() for line in fd.readlines()]
    print('First    : {}'.format(first(lines)))
    print('Second   : {}'.format(second(lines)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
