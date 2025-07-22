from collections import defaultdict

def solution(word, k):
  N = len(word)
  vowels = 'aeiou'
  count = defaultdict(int)
  consonant = 0
  L = result = 0

  for R in range(N):
    # vowel:
    # 1. enough vowels + not enough consonant: continue
    # 2. enough vowels + enough consonant: update result

    if word[R] in vowels:
      count[word[R]] += 1

      if consonant == k and len(count)==len(vowels):
        result += 1

    else:
      # consonant:
      # 1. enough vowels + k consonant: update result + no shrink
      # 2. enough vowels + k+1 consonants: shrink until k consonants are left
      consonant += 1

      while consonant > k:
        if word[L] in vowels:
          count[word[L]] -= 1

          if count[word[L]] == 0:
            del count[word[L]]

        else:
          consonant -= 1

        L += 1

      # consonant = 1
      if len(count)==len(vowels):
        result += 1

  return result

word = 'aeioqq'
k = 1
print(solution(word, k), ', expected: 0')
word = 'aeiou'
k = 0
print(solution(word, k), ', expected: 1')
word = 'ieaouqqieaouqq'
k = 1
print(solution(word, k), ', expected: 3')