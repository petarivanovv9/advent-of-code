import os
from dataclasses import dataclass

DIRECTIONS: dict[str, tuple[int, int]] = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}


@dataclass
class Point:
    x: int
    y: int

    def add(self, direction_x: int, direction_y: int) -> "Point":
        return Point(self.x + direction_x, self.y + direction_y)

    def distance(self, other_point) -> int:
        return abs(self.x - other_point.x) + abs(self.y - other_point.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

visited = set()

head = Point(0, 0)
tail = Point(0, 0)

for line in lines:
    d_raw, s_raw = line.split()
    direction, steps = DIRECTIONS[d_raw], int(s_raw)
    direction_x, direction_y = direction

    for _ in range(steps):
        head = head.add(direction_x, direction_y)

        if (head.x == tail.x and abs(head.y - tail.y) == 2) or (head.y == tail.y and abs(head.x - tail.x) == 2):
            tail = tail.add(direction_x, direction_y)
        elif head.distance(tail) == 3:
            min_dist = None
            new_tail = tail

            for move_x, move_y in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                new_dist = head.distance(tail.add(move_x, move_y))

                if min_dist != None and new_dist <= min_dist:
                    min_dist = new_dist
                    new_tail = tail.add(move_x, move_y)
                elif min_dist == None:
                    min_dist = new_dist
                    new_tail = tail.add(move_x, move_y)

            tail = new_tail

        visited.add(tail)

print('Res:', len(visited))
