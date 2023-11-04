#!/usr/bin/env python3

from typing import Callable


def part1() -> None:
    # Who beats who
    rules: dict[str, str] = {
        "X": "C", # Rock
        "Y": "A", # Paper
        "Z": "B"  # Scissors
    }

    def play_round(op: str, me: str) -> int:
        score: int = (lambda x: ord(x) - 87)(me)

        # win
        if rules[me] == op:
            return score + 6

        # draw
        if ord(op) - ord(me) + 23 == 0:
            return score + 3

        # lose
        return score


    with open("./input.txt", "rt") as fd:
        print(
            sum(
                map(
                    lambda x: play_round(*x.split(" ")),
                    filter(
                        lambda x: x != "",
                        "".join(fd.read()).split("\n")
                    )
                )
            )
        )

def part2() -> None:
    instructions: dict[str, Callable] = {
        "X": (lambda ss: ss + 0), # lose
        "Y": (lambda ss: ss + 3), # draw
        "Z": (lambda ss: ss + 6)  # win
    }
    shape_scores: dict[str, int] = {
        "A": 1, # Rock
        "B": 2, # Paper
        "C": 3  # Scissors
    }
    rules: dict[str, str] = {
        "A": "B", # Rock
        "B": "C", # Paper
        "C": "A"  # Scissors
    }
    falsy_rules: dict[str, str] = {
        "A": "C",
        "B": "A",
        "C": "B"
    }

    def play_round(op: str, outcome: str) -> int:
        return instructions[outcome](shape_scores[op if outcome == "Y" else rules[op] if outcome == "Z" else falsy_rules[op]])

    with open("./input.txt", "rt") as fd:
        print(
            sum(
                map(
                    lambda x: play_round(*x.split(" ")),
                    filter(
                        lambda x: x != "",
                        "".join(fd.read()).split("\n")
                    )
                )
            )
        )

part1()
part2()

