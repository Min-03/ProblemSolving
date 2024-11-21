from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root: TreeNode) -> list[int]:
    ret = []
    if root is None:
        return ret
    q = deque([root])
    while q:
        ret.append(q[-1].val)
        qSize = len(q)
        for _ in range(qSize):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return ret

def right_side_view2(root: TreeNode) -> list[int]:
    ret = []
    max_lev = [-1]
    helper(root, 0, max_lev, ret)
    return ret

def helper(root, lev, max_lev, ret):
    if root is None:
        return
    if lev > max_lev[0]:
        ret.append(root.val)
        max_lev[0] = lev
    helper(root.right, lev + 1, max_lev, ret)
    helper(root.left, lev + 1, max_lev, ret)