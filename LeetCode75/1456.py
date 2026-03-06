#My Solution
def maxVowels(self, s: str, k: int) -> int:
  vowels = {'a','e','i','o','u'}
  window = s[:k]
  count = 0
  for x in window:
    if x in vowels:
      count += 1
  max_count = count
  for i in range(len(s)-k):
    if s[i] in vowels:
      count -= 1
    if s[i+k] in vowels:
      count += 1
    max_count = max(count, max_count)
  return max_count