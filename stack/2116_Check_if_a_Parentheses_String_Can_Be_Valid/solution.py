def solution(s, locked):
  '''
  Observation: Instead of ()()()(())) think of it as X and () where X is a wildcard (aka with locked 0) and () is actual paranthesis
  with locked as 1.

  Algorithm:
    (1). Use 2 stacks:
      - locked_stack: stores '(' with 1 as locked.
      - unlocked_stack: stores 'X' - wildcard (with 0 as locked)

    (2). For each idx, char:
      - Store idx if char belongs to either locked_stack or unlocked_stack.
      - The remaining case: ')' with locked as 1: We GREEDILY pop out from the locked_stack. If there is no element we then
      consider unlocked_stack.

      Why? It may looks odd. E.g: X ( X X ) X
                                          -> When we are here we pop '(' instead of the closest X.
      We can prove that given string of () and X where num of '(' = num of ')' and even number of X. They can form valid parathensis
      despite we close as the above rule.

      e.g: X (X  X X) X (X )

    (3). At the end we may end up with non-empty locked_stack:
      - We can match locked_stack[-1] with unlocked_stack[-1] as long as locked[-1] < unlocked[-1]
      => Remember we store indices. Aka there is a wildcard after this open '('.

    (4). Check if len(locked) == 0 and len(unlocked) is even.

  Time: O(N)
  Space: O(N)

  '''
  N = len(s)

  # valid paranthesises must have even length
  if N%2 > 0:
    return False

  loc_stk = []
  unl_stk = []


  for i, char in enumerate(s):
    if locked[i] == '0':
      unl_stk.append(i)

    elif char == '(':
      loc_stk.append(i)

    else:
      if len(loc_stk)>0:
        loc_stk.pop()

      elif len(unl_stk)>0:
        unl_stk.pop()

      else:
        return False

  while len(loc_stk)>0 and len(unl_stk)>0 and loc_stk[-1] < unl_stk[-1]:
    loc_stk.pop()
    unl_stk.pop()

  return len(loc_stk)==0 and len(unl_stk)%2==0






s = "))()))"
locked = "010100"
print(solution(s, locked), ' expected: True')

s = "()()"
locked = "0000"
print(solution(s, locked), ' expected: True')

s = ")"
locked = "0"
print(solution(s, locked), ' expected: False')

s = "()))"
locked = "1011"
print(solution(s, locked), ' expected: True')

s = "(((())(((())"
locked = "111111010111"
print(solution(s, locked), ' expected: True')

s = "(((()()))))("
locked = "100011011001"
print(solution(s, locked), ' expected: False')