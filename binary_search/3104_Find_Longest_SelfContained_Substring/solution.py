from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(s):
  # loc[char] = [indices]
  loc = defaultdict(list)
  for i, char in enumerate(s):
    loc[char].append(i)

  def check(l, r):
    '''
    Observation:
      (1). Given a window [L, R] how can we check if it's valid.
        - [L, R] is valid iff it doesn't cover any characters partially. In other words
        for each char, either it covers all or it doesnt cover at all.

      => Notice for each char: indices = [sorted list in ascending order]
      => Given [L, R] and char: we can check if [L, R] cover all chars based on indices[]
      using bisect_left and bisect_right.

      (2). To find L, R we can narrow it down to L = first occurence of each character, R = last
      occurence of each character.
      => for c1 in indices:
            for c2 in indices:
              (L = indices[c1][0], R = indices[c2][-1])

      By doing this we make sure: Our set of substrings we traverse will be narrower.

    Time: O(N + 26*26*log(N)) where N = len(s)
    Space: O(N*26)

    '''
    '''
    (l, r) - range

    For each char:
      - check if the range (l, r) covers all chars or not at all
      - we dont want (l, r) to partially cover a char.
    '''
    for char in loc:
      '''
      We use bisect_left and bisect_right to find the (x, y) where (x, y)
      is the window with size closest to (l, r) based on the indices of loc[char]

      e.g: indices = [1, 3, 5, 6], l = 2, r = 7
      x = bsl([], 2) = 1
      y = bsr([], 7) = 4 => x, y = ([3, 5, 6]) => cover at most 3 elements

      e.g: indices = [1, 3, 5, 6], l = 0, r = 7
      x = bsl([], 0) => 0
      y = bsr([], 7) => 4 => [1,3,5,6]
      '''

      x, y = bisect_left(loc[char], l), bisect_right(loc[char], r)

      # (l, r) only covers partially.
      if x != y and y-x < len(loc[char]):
        return False

    return True


  result = -1

  # start and end to be first and last occurence.
  for char1 in loc:
    # start index
    l = loc[char1][0]

    for char2 in loc:
      # end index
      r = loc[char2][-1]

      # check range substr (l, r) is valid
      if l > r or r-l+1 == len(s): continue

      if check(l, r):
        result = max(result, r-l+1)

  return result
#--------------------------
s = 'abba'
print(solution(s))
