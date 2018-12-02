
from itertools import cycle
from typing import List


def part1(input: List[int]) -> int:
    return sum(input)


def part2(input: List[int]) -> int:
    seen = set([0])
    res = 0

    for val in cycle(input):
        res += val

        if res in seen:
            return res

        seen.add(res)


def _load_input() -> List[int]:
    with open('d01/input.txt', 'r') as f:
        content = f.read()
    return list(map(int, content.strip().split('\n')))


def _main():
    input_data = _load_input()
    print(f'Part 1: {part1(input_data)}')
    print(f'Part 2: {part2(input_data)}')


if __name__ == '__main__':
    _main()
