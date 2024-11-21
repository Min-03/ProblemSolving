from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, dic):
        i_root = 0
        if i_root not in dic:
            return
        self.root = TreeNode(dic[i_root])
        q = deque([(i_root, self.root)])
        while q:
            i_curr, curr = q.popleft()
            i_left = i_curr * 2 + 1
            if i_left in dic:
                child = TreeNode(dic[i_left])
                q.append((i_left, child))
                curr.left = child
            i_right = i_curr * 2 + 2
            if i_right in dic:
                child = TreeNode(dic[i_right])
                q.append((i_right, child))
                curr.right = child

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def level_with_min_sum(node):
    # TODO
    q = deque()
    q.append(node)
    lo, lo_idx = 1e9, -1
    idx = 0
    while q:
        size = len(q)
        ssum = 0
        for _ in range(size):
            curr = q.popleft()
            ssum += curr.val
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        if (lo > ssum):
            lo = ssum
            lo_idx = idx
        idx += 1
    return lo_idx

def level_with_min_sum_ver2(nodes):
    i_root = 0
    q = deque()
    q.append(i_root)
    lo, lo_idx = float("inf"), -1
    idx = 0
    while q:
        qSize = len(q)
        ssum = 0
        for _ in range(qSize):
            curr = q.popleft()
            ssum += nodes[curr]
            if curr * 2 + 1 in nodes:
                q.append(curr * 2 + 1)
            if curr * 2 + 2 in nodes:
                q.append(curr * 2 + 2)
        if ssum < lo:
            lo = ssum
            lo_idx = idx
        idx += 1
    return lo_idx
     

if __name__ == '__main__':
    nodes = {0:8, 1:2, 2:3, 5:1, 6:5, 11:24}
    T = Tree(nodes)
    result = level_with_min_sum(T.root)
    print(result)
    print (level_with_min_sum_ver2(nodes))

