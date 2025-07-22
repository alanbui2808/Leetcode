def solution(source, target):
  '''
  Algorithm: Greedily
  (1). We traverse from left to right, greedily construct the longest subsequence to construct the target string.
  (2). Everytime we meet a character, we need to make sure it's in the source string and the position[character] >
  position[previous_character] (compared in the source string). If yes then we can extend the current subsequence
  that we built.

  Problem: We need to effeciently determine if there is character appears after position[previous_character]+1 in the source
  string. We can do this in O(1) time by preprocessing as following:

  For each character in the source string:
  next_char[char][i] = next position of "char" starting at i (-1 if there is no)
  Formula: next_char[char][i] = i if source[i] == char else next_char[char][i-1]

  e.g: aba --> [0 2 2]

  Time complexity: O(len(26*source) + len(target))
  '''
  M = len(source)
  N = len(target)
  # dict[i][char]: next position of "char" starting at i (-1 if there is no)
  # O(26*M) since there can be at most 26 characters
  next_char = {}
  for char in source:
    next_char[char] = [-1 for i in range(M)]
    # Initialize the base case
    next_char[char][-1] = -1 if source[-1] != char else M-1
    for i in reversed(range(M-1)):
      # update next_char[char][i]
      next_char[char][i] = next_char[char][i+1] if source[i] != char else i

  result = i = 0
  cur_sequence = [] # store the indices (in the source) of char, make sure it's increasing

  # O(N)
  while i < N:
    char = target[i]
    if char not in source:
      return -1

    if len(cur_sequence) == 0:
      # get the first position that char appears in source, guarantee it exists (not -1)
      cur_sequence.append(next_char[char][0])
      i += 1
      continue

    # get the position of the previous_char
    prev_char_position = cur_sequence[-1]
    # check if char appears after this position
    if prev_char_position < M-1 and next_char[char][prev_char_position+1] != -1:
      cur_sequence.append(next_char[char][prev_char_position+1])
      i += 1
    else:
      result += 1
      # reset cur_sequence
      cur_sequence = []
      # remain i

  return result+1 if len(cur_sequence)>0 else result

source = input()
target = input()
print(solution(source, target))
