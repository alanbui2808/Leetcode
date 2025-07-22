def solution(s, k):
  '''
  s = ""
  k = int

  choose k characters in s and uppercase them to another char.

  return leng of longest substr containing same letter with k ops.

  for each letter char, do sliding window [L, R]:
    1. Expand the window [L, R] and keep track of # chars != char
    2. Record the length.
    3. Shrink [L, R] if diff > k

  Time: O(26N) = O(N)
  '''
  N = len(s)

  def longest_substr(char):
    L = 0
    diff = 0
    longest = 0


    for R in range(N):
      if s[R] != char:
        diff += 1

      while diff > k:
        if s[L] != char:
          diff -= 1

        L += 1

      # count all cases with diff <= k
      longest = max(longest, R-L+1)

    return longest



  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = 0

  for char in letters:
    result = max(result, longest_substr(char))

  return result

s = 'ABAB'
k = 2
print(solution(s, k), ', expected: 4')
s = 'AABABBA'
k = 1
print(solution(s, k), ', expeted: 4')
s = 'BBAAA'
k = 2
print(solution(s, k), ', expeted: 5')
s = 'AAAA'
k = 2
print(solution(s, k), ', expeted: 4')