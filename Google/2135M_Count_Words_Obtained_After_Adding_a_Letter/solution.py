class TrieNode:
  def __init__(self):
    self.child, self.end = {}, False

class Trie:
  def __init__(self):
    self.trie = TrieNode()

  def insert(self, word):
    temp = self.trie

    for char in word:
      if char not in temp.child:
        temp.child[char] = TrieNode()
      temp = temp.child[char]

    # Mark the end of a word
    temp.end = True

  def search(self, word):
    # allow to skip once
    temp = self.trie

    for char in word:
      if char not in temp.child:
        return False
      temp = temp.child[char]

    return temp.end
#-----------------------------------------
def solution(start_words, target_words):
  '''
  (1). Sort all the words in both start_words and target_words so that all the arrangement are uniform. O(N*log(26) + Mlog(26))
  (2). Construct a trie from start_words
  (3). For each target_words, we remove a character from it and then start searching in the trie.

  Time Complexity: O(Nlog(26) + Mlog(26) + N)
  '''
  N = len(start_words)

  dictionary = Trie()

  for i in range(N):
    start_words[i] = sorted(start_words[i])
    dictionary.insert(start_words[i])
    target_words[i] = sorted(target_words[i])

  result = 0

  # O(N*26*26)
  for word in target_words:
    # O(26)
    for i in range(len(word)):
      new_word = ''.join(word[:i] + word[i+1:])
      # O(26)
      can_converse = dictionary.search(new_word)
      if can_converse:
        result += 1
        break

  return result

start_words = ["ab", "a"]
target_words = ["abc", "abcd"]
print(solution(start_words, target_words))
