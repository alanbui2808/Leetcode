def solution(s):
  '''
  Observation: Stack implementation

  Time: O(3N) - if we construct substring following below implementation each character/element will be traverse at most 3 times:
    (1). When add to stk
    (2). Pop out of stk
    (3). Reverse when substr construction.
  '''
  N = len(s)
  stk = []

  for c in s:
    if c.isdigit() or c == '[' or c.isalpha():
      stk.append(c)

    if c == ']':
      tmp = []

      # pop until stk[-1].isdigit()
      while len(stk)>0 and not stk[-1].isdigit():
        if stk[-1].isalpha():
          tmp.append(stk[-1]) # O(1)

        stk.pop() # O(1)

      # construct k (k >= 1 digits)
      k = []
      while len(stk)>0 and stk[-1].isdigit():
        k.append(stk[-1])
        stk.pop()

      k.reverse() # O(N)
      tmp.reverse() # more efficient than insert(0, c[-1])
      k = int(''.join(k))

      stk.append(''.join(tmp)*k) # O(1)

  return ''.join(stk)
#----------------------------------

s = "3[a]2[bc]"
print(solution(s), ' expected: aaabcbc')

s = "3[a2[c]]"
print(solution(s), ' expected: accaccacc')

s = "2[abc]3[cd]ef"
print(solution(s), ' expected: abcabccdcdcdef')

s = "10[leetcode]"
print(solution(s), ' expected: 2leetcode')