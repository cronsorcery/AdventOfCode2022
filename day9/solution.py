from typing import Generator, TypeAlias

pos_t: TypeAlias = tuple[int, int]

def read_command(fname: str) -> Generator[tuple[str, str, str], None, None]:
    with open(fname) as fd:
        while line := fd.readline().strip().partition(" "):
            *_, amount = line
            if not amount: break
            yield line


def move_head(head: pos_t, direction: str) -> pos_t:
    hx, hy = head
    if direction == "R":
        hx += 1
    elif direction == "L":
        hx -= 1
    elif direction == "U":
        hy += 1
    elif direction == "D":
        hy -= 1
    else:
        raise Exception(f"Illegal instruction {direction = }")
    return hx, hy


def move_tail(head: pos_t, tail: pos_t) -> pos_t:
    hx, hy = head
    tx, ty = tail
    dx = hx - tx
    dy = hy - ty
    if max(abs(dx), abs(dy)) > 1:
        tx += dx // abs(dx) if dx else 0
        ty += dy // abs(dy) if dy else 0
    return tx, ty


def part1() -> int:
    head = (0, 0)
    tail = (0, 0)
    visited = set()
    for direction, _, amount in read_command("./input.txt"):
        for _ in range(int(amount)):
            head = move_head(head, direction)
            tail = move_tail(head, tail)
            visited.add(tail)
    return len(visited)

def part2() -> int:
    rope = [(0, 0) for _ in range(10)]
    visited = set()
    for direction, _, amount in read_command("./input.txt"):
        for _ in range(int(amount)):
            rope[0] = move_head(rope[0], direction) # type: ignore
            for i, _ in enumerate(rope[1:], 1):
                rope[i] = move_tail(rope[i-1], rope[i]) # type: ignore
            visited.add(rope[-1])
    return len(visited)

def main() -> int | str:
    print(part1())
    print(part2())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
