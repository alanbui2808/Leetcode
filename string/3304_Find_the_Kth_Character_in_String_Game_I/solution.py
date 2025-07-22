def solution(k):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  n = len(letters)
  s = ['a']

  while len(s) < k+1:
    m = len(s)


    for i in range(m):
      cur_char = s[i]
      cur_idx = letters.index(cur_char)
      new_idx = (cur_idx+1)%n

      new_char = letters[new_idx]
      s.append(new_char)

  return s[k-1]
#--------------------------------------
print(solution(5), ' expected: b')
print(solution(10),' expected: c')
