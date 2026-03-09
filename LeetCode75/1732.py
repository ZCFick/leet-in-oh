#My solution (100%)
def largestAltitude(gain: list[int]) -> int:
  alt, max_alt = 0, 0
  for g in gain:
    alt += g
    max_alt = max(alt,max_alt)
  return max_alt