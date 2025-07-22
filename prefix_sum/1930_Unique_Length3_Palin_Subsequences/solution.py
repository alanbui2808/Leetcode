def solution(s):
  '''
  Algorithm: For cur_char at i, we need to find:
    (1). Closest char (a-z) from [0, i-1]. O(26)
    (2). If there such char exists in (1) at index j, then find closest cur_char from [0, j-1]. O(1)

    We are interested in 3-length palindrome.
    Edge case: If aba is found at point, that means (b)-(a) is formed. Later on if we get to (b)-(a) again we can ignore

    Thus, we need to pre-compute closest[char][i]. O(26*N)

  Time complexity: O(26*N)
  Space: O(26*N)

  '''
  alphabets = 'abcdefghijklmnopqrstuvwxyz'
  n = len(s)
  # closest[char][i] = closest char w.r.t i from (0 -> i)
  closest = {char: [-1]*n for char in alphabets} # {char: [-1] of len(s)}
  # used for line 35
  middle = {char:[] for char in alphabets} # {char: [list of a-z]}
  result = 0

  for i in range(n):
    cur_char = s[i]

    # only update closest[char][i] = i (index) where char = cur_char
    for char in alphabets:
      if cur_char == char:
        closest[char][i] = i
      else:
        closest[char][i] = closest[char][i-1] if i-1>=0 else -1


  for i in range(2, n):
    cur_char = s[i]

    for char in alphabets:
      # if char in middle[cur_char] then it means the string "(cur_char) char (cur_char)" has been formed previously
      if char in middle[cur_char]:
        continue

      # exists a palindrome: "(cur_char) char (cur_char)"
      j = closest[char][i-1]

      if j in range(0, i):
        k = closest[cur_char][j-1]

        if k in range(0, j):
          middle[cur_char].append(char)
          result += 1


  return result

s = input()
print(solution(s))



