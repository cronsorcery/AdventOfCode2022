#!/usr/bin/env python3

from itertools import starmap

def get_item_priority(item: str) -> int:
    return ord(item) - 96 if item.islower() else ord(item) - 38


def part1() -> None:
    with open("./input.txt", "rt") as fd:
        print(sum(map(
                    lambda x: get_item_priority(next(iter(set(x[:len(x)//2]) & set(x[len(x)//2:])))),
                    filter(lambda x: x != "", "".join(fd.read()).split("\n")))))


def part2() -> None:
    with open("./input.txt", "rt") as fd:
        print(sum(starmap(
                    lambda a, b, c: get_item_priority(next(iter(set(a) & set(b) & set(c)))),
                    zip(*[filter(lambda x: x != "", "".join(fd.read()).split("\n"))] * 3))))

part1()
part2()
