#My solution
def closeStrings(word1: str, word2: str) -> bool:
  w1 = dict()
  w2 = dict()
  for letter in word1:
    w1[letter] = w1.get(letter, 0) + 1
  for letter in word2:
    w2[letter] = w2.get(letter, 0) + 1
  return w1.keys() == w2.keys() and sorted(w1.values()) == sorted(w2.values())