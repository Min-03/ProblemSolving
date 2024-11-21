import sys
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
class Tree:
    def __init__(self, root=None):
        self.root = root

def minimalTree(arr: list[int]):
    buildTree(arr, 0, len(arr) - 1)

def buildTree(arr, l, r):
    if l > r:
        return None
    mid = (l + r) // 2
    return TreeNode(arr[mid], buildTree(arr, l, mid - 1), buildTree(arr, mid + 1, r))

def printInorder(node):
    if node:
        printInorder(node.left)
        print(node.data)
        printInorder(node.right)

# def reconstructTree(preorder, inorder):
#     def helper(l, n, prev):
#         if n <= 0:
#             return None
#         val = preorder[l]
#         curr = str2idx[val]
#         n_left = curr - prev - 1 if curr > prev else n - prev + curr
#         n_right = n - curr + prev if curr > prev else prev - curr - 1
#         left = helper(l + 1, n_left, curr)
#         right = helper(l + 1 + n_left, n_right, curr)
#         return TreeNode(val, left, right)
#     str2idx = {x: i for i, x in enumerate(inorder)}
#     return helper(0, len(preorder), -1)

def reconstructTree(postorder, inorder):
    def helper(r, n, prev):
        if n <= 0:
            return None
        val = postorder[r]
        curr = str2idx[val]
        n_left = curr - prev - 1 if curr > prev else n - prev + curr
        n_right = n - curr + prev if curr > prev else prev - curr - 1
        left = helper(r - 1 - n_right, n_left, curr)
        right = helper(r - 1, n_right, curr)
        return TreeNode(val, left, right)
    str2idx = {x: i for i, x in enumerate(inorder)}
    return helper(len(inorder) - 1, len(inorder), -1)




    
# def _reconstructTree(preorder: list[str], inorder: list[str], inorderPos: dict[str, int], pl: int, pr: int, il: int, ir: int):
#     if pl > pr:
#         return None
#     rootVal = preorder[pl]
#     idx = inorderPos[rootVal]
#     left = idx - il
#     root = TreeNode(rootVal)
#     root.left = _reconstructTree(preorder, inorder, inorderPos, pl + 1, pl + left, il, idx - 1)
#     root.right = _reconstructTree(preorder, inorder, inorderPos, pl + left + 1, pr, idx + 1, ir)
#     return root


# def reconstructTree(preorder: list[str], inorder: list[str]):
#     inorderPos = {ch : i for i, ch in enumerate(inorder)}
#     return _reconstructTree(preorder, inorder, inorderPos, 0, len(preorder) - 1, 0, len(inorder) - 1)

# def reconstructTree_old(preorder, inorder):
#     if not preorder:
#         return None
#     root = TreeNode(preorder[0])
#     pos = inorder.index(preorder[0])
#     root.left = reconstructTree_old(preorder[1: pos + 1], inorder[0: pos])
#     root.right = reconstructTree_old(preorder[pos + 1:], inorder[pos + 1:])
#     return root
    

if __name__ == "__main__":
    arr = [2, 3, 4, 5, 6, 7, 8, 9]
    root = minimalTree(arr)
    preorder = "a b d e c f g".split()
    postorder = "d e b f g c a".split()
    inorder = "d b e a f c g".split()
    root = reconstructTree(postorder, inorder)
    # root = reconstructTree_old(preorder, inorder)
    printInorder(root)
