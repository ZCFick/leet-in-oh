#My solution using zip for transpose matrix
def equalPairs(grid: list[list[int]]) -> int:
  rows = dict()
  for row in grid:
    rows[tuple(row)] = rows.get(tuple(row), 0) + 1
  count = 0
  for col in zip(*grid):
    count += rows.get(tuple(col), 0)
  return count