from typing import Generator

def read_instruction(fname: str) -> Generator[tuple[str, str, str], None, None]:
    with open(fname) as fd:
        while line := fd.readline().strip():
            yield line.partition(" ")

def calculate_signal_strength(cycle: int, X: int) -> int:
    return cycle * X if cycle in (20, 60, 100, 140, 180, 220) else 0

def draw_screen(cycle: int, crt_row: int, X: int) -> int:
    if not cycle % 40:
        crt_row += 1
        print()
    if cycle % 40 - 1 <= X <= cycle % 40 + 1:
         print("#", end="")
    else:
        print(".", end="")
    return crt_row

def main() -> int | str:
    cycle = 0
    X = 1 # Horiziontal position of the middle of 3-pixel sprite
    tss = 0
    crt_row = 0

    for op, _, param in read_instruction("./input.txt"):
        if op == "noop":
            crt_row = draw_screen(cycle, crt_row, X)
            cycle += 1
            tss += calculate_signal_strength(cycle, X)
        elif op == "addx":
            for _ in range(2):
                crt_row = draw_screen(cycle, crt_row, X)
                cycle += 1
                tss += calculate_signal_strength(cycle, X)
            X += int(param)
        else:
            raise Exception(f"Illega instruction {op = }")

    print()
    print(tss)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
