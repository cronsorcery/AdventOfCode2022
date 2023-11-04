#!/usr/bin/env python3

from itertools import islice


def part1() -> None:
    """
    Max sum
    """
    with open("./input.txt", "rt") as fd:
        print(
            max(
                map(
                    lambda x: sum(map(int, x)),
                    (
                        elf.strip().split("\n") for elf in "".join(
                            line for line in fd.read()
                        ).split("\n\n")
                    )
                )
            )
        )

def part2() -> None:
    """
    Sum of top 3 sums
    """
    with open("./input.txt", "rt") as fd:
        print(
            sum(
                islice(
                    sorted(
                        map(
                            lambda x: sum(map(int, x)),
                            (
                                elf.strip().split("\n") for elf in "".join(
                                    line for line in fd.read()
                                ).split("\n\n")
                            )
                        ),
                        reverse=True
                    ),
                    3
                )
            )
        )

part1()
part2()

