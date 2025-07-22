def solution(s, indices, sources, targets):
  '''
  Time Complexity: O(resulted string)
  In the worst case, we have to delete all characters in s and replace with new string, thus O(S + T) where T is the length
  new string and S is the length of old string.
  '''
  result = list(s)

  for index, source, target in zip(indices, sources, targets):
    # if we can replace starting starting at this index
    if s[index : index+len(source)] == source:
      # we store target string in result[index]
      result[index] = target
      # We delete the old characters
      # Let's say s = 'list', result = [l, i, s, t] indices = [1], source = [i] and target = ['target']
      # then at index 1 we can replace 'i' with 'target', we perform by:
      # result = [l, target, s, t], this is clever because once we call ''.join at the end it will be correct.
      # we just need to delete substring that matches the source and store the target the first index that matches
      # source.
      # e.g2: [a,b,c,d], indices = [0], source = 'ab', target='target' then result = [target, c, d], we delete a, b
      # once we ''.join(result) at the end it is still correct
      for i in range(index+1, index+len(source)):
        result[i] = ''

  return ''.join(result)
#--------------------------------------------
s = input()
indices = list(map(int, input().split()))
sources = input().split()
targets = input().split()
print(solution(s, indices, sources, targets))
