from collections import defaultdict

def solution(s, max_letters, min_size, max_size):
  N = len(s)

  '''
  Observation:
    (1). Sliding Window [L, R]
    (2). Maintain a window [L, R]:
      - if len(count) <= max_letters or R-L+1 == min_size: Record s[L:R+1] occurence and update result

      - If len(count) > max_letters or R-L+1 > min_size: we must shrink L
        Note: We strictly keep len([L, R]) <= min_size because: Suppose we have a valid [L, R]:
        e.g: aaab, max_letters = 2, min = 2, max = 4

        If we keep expanding aaab and only shrink when R-L+1 >= max_size, then we could only record
        occurence of aaab, aab and misses ab. Hence we greedily count the shortest valid substr

        There is no way aaab (or aab) might occur more than ab because ab is inside these strings.

  Time: O(N + min_size*N), sliding window is O(N), min_size <= 26
  Space: O(26N)
  '''

  count = defaultdict(int)
  occ = defaultdict(int)

  L = 0
  result = 0

  for R in range(N):
    count[s[R]] += 1

    '''
    Shrink if either:
      1. len(count) > max_letters
      2. R-L+1 > min_size
    '''
    while L < R and (len(count)>max_letters or R-L+1>min_size):
      count[s[L]] -= 1
      if count[s[L]] == 0:
        del count[s[L]]

      L += 1

    # len(count) <= max_letters and R-L+1 <= min_size
    # However we interested in: len(count) <= max_letters and R-L+1 == min_size
    if R-L+1 == min_size:
      substr = s[L:R+1]
      occ[substr] += 1
      result = max(result, occ[substr])

  return result
#-------------------------------------
s = "aababcaab"
max_letters = 2
min_size = 3
max_size = 4
print(solution(s, max_letters, min_size, max_size), ', expected: 2')
s = "aaaa"
max_letters = 1
min_size = 3
max_size = 3
print(solution(s, max_letters, min_size, max_size), ', expected: 2')
s = "aabcabcab"
max_letters = 2
min_size = 2
max_size = 3
print(solution(s, max_letters, min_size, max_size), ', expected: 3')
