# --- Day 3: Spiral Memory ---
#
# You come across an experimental new kind of memory stored on an infinite two-dimensional grid.
#
# Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up
# while spiraling outward. For example, the first few squares are allocated like this:
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
#
# While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1
# (the location of the only access port for this memory system) by programs that can only move up, down, left, or
# right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.
#
# For example:
#
#     Data from square 1 is carried 0 steps, since it's at the access port.
#     Data from square 12 is carried 3 steps, such as: down, left, left.
#     Data from square 23 is carried only 2 steps: up twice.
#     Data from square 1024 must be carried 31 steps.
#
# How many steps are required to carry the data from the square identified in your puzzle input
# all the way to the access port?
from itertools import cycle


input = 277678

def move_up(x, y):
    return x, y + 1

def move_down(x, y):
    return x, y - 1

def move_right(x, y):
    return x + 1, y

def move_left(x, y):
    return x - 1, y

move_order = [move_right, move_up, move_left, move_down]

def gen_grid(size):
    moves = cycle(move_order)
    num_moves = 1
    x = 1
    starting_pos = 0, 0

    yield x, starting_pos

    while True:
        for g in range(2):
            move = next(moves)
            for g in range(num_moves):
                if x >= size:
                    return
                starting_pos = move(* starting_pos)
                x += 1
                yield x, starting_pos
        num_moves += 1

def distance_from_center(block):
    bx, by = block
    return abs(bx - 0) + abs(by - 0)

day3_grid = list(gen_grid(input))

print(distance_from_center(day3_grid[-1][-1]))
