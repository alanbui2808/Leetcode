from collections import defaultdict, Counter

def solution(s):
  '''
  Observation: Greedy + Stack
    1. At current char, we maintain a stack that represents the smallest lex order string.
    2. We keeps popping stk[-1] if these 2 conditions meet:
      - stk[-1] >= char: greedily picks the smaller char.
      - rem[-1] > 0: there are remaining characters later.
      e.g: stk = [a c d] cur_char = b. Can only pop 'd' if 'd' > 'b' AND remaining 'd' > 0.
    3. Add cur_char to stk and mark used[cur_char]

  Time: O(N)
  Space: O(N)


  '''
  s = list(s)
  N = len(s)
  stk = []
  rem = Counter(s)
  used = defaultdict(int)

  for char in s:
    rem[char] -= 1
    if used[char]>0: # char already used aka in stk, we ignore
      continue

    while stk and ord(stk[-1])>=ord(char) and rem[stk[-1]]>0:
      rmv = stk.pop()
      used[rmv] -= 1


    stk.append(char)
    used[char] += 1


  return "".join(stk)
#----------------------------------------
s = "bcabc"
print(solution(s), " expected: abc")
s = "cbacdcbc"
print(solution(s), " expected: acdb")
s = "bbcaac"
print(solution(s), " expected: bac")


