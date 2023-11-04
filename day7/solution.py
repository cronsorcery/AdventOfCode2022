#!/usr/bin/env python3


def execute(inp: list[str]) -> dict[str, int]:
    fs: dict[str, int] = {}
    pwd: list[str] = []

    for line in inp:
        match line.strip().split():
            case ["$", "cd", ".."]:
                pwd.pop()
            case ["$", "cd", "/"]:
                pwd = ["/"]
            case ["$", "cd", dir]:
                pwd.append(dir)
            case ["$", "ls"] | ["dir", *_]:
                continue
            case [size, _]:
                current_path = ""
                for dir in pwd:
                    if current_path != "/" and dir != "/":
                        current_path += "/"
                    current_path += dir
                    fs[current_path] = fs.get(current_path, 0) + int(size)
            case []:
                break

    return fs

def part1() -> None:
    with open("input.txt", "rt") as fd:
        fs: dict[str, int] = execute(fd.read().split("\n"))
        print(sum(filter(lambda x: x < 100_000, fs.values())))
        print(min(filter(lambda x: x >= 30_000_000 - (70_000_000 - fs["/"]), fs.values())))


part1()

