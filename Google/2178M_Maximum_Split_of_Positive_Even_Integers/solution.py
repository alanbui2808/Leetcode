def solution(final_sum):
  '''
  Algorithm:
  (1). We grow our a current_sum by slowing adding i until the sum exceeds the final_sum. Note that: i = i + 2 every time.
  (2). remaining = final_sum - current_sum, we add this amount to the final element.

  e.g: 28 -> [2, 4, 6, 10], current_sum = 22, remaining = 28 - 22 = 6 --> we add 6 to 10: [2,4,6,16]
  Note that we could distribute 6 into [2, 6(4+2), 8(6+2), 12(10+2)] but that the maximum splits still dont change.

  Time complexity: O(final_sum^0.5), current_sum = 2 + 4 + ... + (i+2) = i(2+(i+2)) // 2 = i^2. i^2 ~ final_sum thus O(final_sum^0.5)
  '''
  result = []
  current_sum = 0
  i = 2

  if final_sum % 2 == 1:
    return []

  while current_sum + i <= final_sum:
    result.append(i)
    current_sum += i
    i += 2

  result[-1] += (final_sum - current_sum)

  return result

final_sum = int(input())
print(solution(final_sum))
