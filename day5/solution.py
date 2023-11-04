#!/usr/bin/env python3

import re
from itertools import zip_longest, starmap

instruction_pattern: re.Pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")


def split_input(inp: list[str]) -> tuple[list[str], list[str]]:
    return inp[:inp.index("")], inp[inp.index(""):][1:]


def create_stacks(inp: list[str]) -> dict[str, list[str]]:
    return {
        i[0]: [j for j in i[::-1][:-1] if j and j != " "]
            for i in zip_longest(
                list(inp[-1].strip())[::4],
                    *map(
                        lambda x: list(x.removeprefix("[").removesuffix("]").removeprefix(" ").removesuffix(" ")[::4]),
                        inp[:-1:]
            )
        )
    }



def part1() -> None:
    def process_instructions(stacks: dict[str, list[str]], instructions: list[str]) -> dict[str, list[str]]:
        """
        -> move x from y to z
                ^      ^    ^
                n      stack1 -> stack2
        """
        if len(instructions) <= 1:
            return stacks

        n_crates, source, target = instruction_pattern.match(instructions[0]).groups() # type: ignore
        stacks[target] += [stacks[source].pop() for _ in range(int(n_crates))]

        return process_instructions(stacks, instructions[1:])


    with open("./input.txt", "rt") as fd:
        print("".join(v[-1] for v in next(starmap(lambda a, b: process_instructions(create_stacks(a), b), [split_input("".join(fd.read()).split("\n"))])).values()))


def part2() -> None:
    def process_instructions(stacks: dict[str, list[str]], instructions: list[str]) -> dict[str, list[str]]:
        """
        -> move x from y to z
                ^      ^    ^
                n      stack1 -> stack2
        """
        if len(instructions) <= 1:
            return stacks

        n_crates, source, target = instruction_pattern.match(instructions[0]).groups() # type: ignore
        n_crates: int = len(stacks[source])-int(n_crates)
        stacks[target] += stacks[source][n_crates:]
        del stacks[source][n_crates:]

        return process_instructions(stacks, instructions[1:])


    with open("./input.txt", "rt") as fd:
        print("".join(v[-1] for v in next(starmap(lambda a, b: process_instructions(create_stacks(a), b), [split_input("".join(fd.read()).split("\n"))])).values()))


part1()
part2()

