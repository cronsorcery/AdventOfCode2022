#!/usr/bin/env python3

from itertools import starmap

def to_range(sr: str) -> range:
    min_range, max_range = sr.split("-")
    return range(int(min_range), int(max_range)+1)


def part1() -> None:
    with open("./input.txt", "rt") as fd:
        print(
            list(
                starmap(
                    lambda a, b: all(i in to_range(a) for i in list(to_range(b))) or all(i in to_range(b) for i in list(to_range(a))),
                    map(lambda x: x.split(","), "".join(fd.read()).strip().split("\n")))).count(True))

def part2() -> None:
    with open("./input.txt", "rt") as fd:
        print(
            list(
                starmap(
                    lambda a, b: any(set(list(to_range(a))) & set(list(to_range(b)))),
                    map(lambda x: x.split(","), "".join(fd.read()).strip().split("\n")))).count(True))

part1()
part2()

