from argparse import ArgumentParser
from enum import Enum


class Action(Enum):
    Forward = 1
    Up      = 2
    Down    = 3

    def __str__(self):
        if self == Action.Forward:
            return 'Forward'
        elif self == Action.Up:
            return 'Up'
        elif self == Action.Down:
            return 'Down'
        else:
            return ''


class State(object):
    def __init__(self):
        self.vertical   = 0
        self.horizontal = 0

    def update(self, actions):
        if type(actions) is list:
            for action in actions:
                self.update(action)
        else:
            x, v = actions
            if x == Action.Forward:
                self.horizontal += v
            elif x == Action.Up:
                self.vertical -= v
            elif x == Action.Down:
                self.vertical += v

    def __str__(self):
        return 'Vertical: {} - Horizontal: {}'.format(
                self.vertical
                , self.horizontal
                )


def parse(line):
    line            = line.strip()
    action, units   = line.split(' ')

    if action == 'forward':
        return (Action.Forward, int(units))
    elif action == 'up':
        return (Action.Up, int(units))
    elif action == 'down':
        return (Action.Down, int(units))
    else:
        raise ValueError('unexpected action')


def main(args):
    # Reads and parses input
    with open(args.file, 'r') as fd:
        xs = fd.readlines()
    ys      = [parse(x) for x in xs]

    # Generates state handler
    state   = State()
    # Updates state
    state.update(ys)

    # Solves part 1
    print(state.vertical * state.horizontal)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    main(parser.parse_args())
