def solution(s, x, y):
  N = len(s)
  stk = []
  res = 0
  k = x if x > y else y

  for char in s:
    if char != 'a' and char != 'b':
      stk.append(char)
      continue

    # ab
    if k == x:
      if char == 'b' and stk and stk[-1]=='a':
        stk.pop()
        res += x
      else:
        stk.append(char)

    # ba
    if k == y:
      if char == 'a' and stk and stk[-1]=='b':
        stk.pop()
        res += y
      else:
        stk.append(char)

  while len(stk)>1:
    while stk and stk[-1] not in ('a', 'b'):
      stk.pop()
    c2 = stk.pop() if stk else 'k'
    while stk and stk[-1] not in ('a', 'b'):
      stk.pop()
    c1 = stk.pop() if stk else 'k'

    if k==y and (c1,c2)==('a', 'b'):
      res += x

    if k==x and (c1,c2)==('b', 'a'):
      res += y

  return res
#--------------------------------------
s = "cdbcbbaaabab"
x = 4
y = 5
print(solution(s, x, y), 'expected: 19')
s = "aabbaaxybbaabb"
x = 5
y = 4
print(solution(s, x, y), 'expected: 20')
s = "ababba"
x = 4
y = 5
print(solution(s, x, y), 'expected: 14')
s = "cbaabwbbbabbwaaq"
x = 4074
y = 9819
print(solution(s, x, y), 'expected: 23712')




