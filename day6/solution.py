#!/usr/bin/env python3


def seek_entity(data: list[str], sz: int) -> int:
    return next(filter(lambda x: len(set(data[x:x+sz])) == sz, range(len(data)-sz+1)))+sz


def part1() -> None:
    with open("./input.txt", "rt") as fd:
        print(seek_entity(list(fd.read()), 4))


def part2() -> None:
    with open("./input.txt", "rt") as fd:
        print(seek_entity(list(fd.read()), 14))


part1()
part2()

