class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left, self.right = left, right

def solution(root, s, t):
  def find(node, target, path):
    '''
    (1). We find a path from s to root and t to root. Store their paths.
    (2). We then remove all the common nodes in their paths, this will reduce to their LCA.
    (3). Replace all directions from the s_paths to 'U' and reverse all directions in t_paths

    Time Complexity: O(N) since the worst case we have to traverse all the nodes to find s and t
    '''
    if node is None:
      return False

    if node.val == target:
      return True

    left = find(node.left, target, path)
    right = find(node.right, target, path)
    '''
    3 possibilities:
    (1). in L subtree
    (2). in R subtree
    (3). None (explore the wrong path)

    '''
    # found target in left subtree
    if left:
      path.append('L')
      return True

    # found target in right subtree
    elif right:
      path.append('R')
      return True

  s_path = []
  t_path = []
  find(root, s, s_path)
  find(root, t, t_path)

  # remove common nodes in their path
  while len(s_path)>0 and len(t_path)>0 and s_path[-1]==t_path[-1]:
    s_path.pop()
    t_path.pop()

  for i in range(len(s_path)):
    s_path[i] = 'U'

  return ''.join(s_path+list(reversed(t_path)))

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)

one.left, one.right = two, three

print(solution(one, 2, 3))
