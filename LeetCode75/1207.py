#My solution, beats 100%
def uniqueOccurrences(arr: list[int]) -> bool:
  counts = dict()
  occurs = set()
  for x in arr:
    counts[x] = counts.get(x, 0) + 1
  for x in counts.values():
    if x in occurs:
      return False
    occurs.add(x)
  return True