#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.dfs(root)
        return root

    def dfs(self, root: TreeNode) -> None:
        if root == None:
            return
        self.dfs(root.right) #go to the most right
        self.sum += root.val
        root.val = self.sum
        self.dfs(root.left)
        return #reverese inorder traversal, and add the value