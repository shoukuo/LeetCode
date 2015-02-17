# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    seq = []
    def __init__(self):
        self.seq = []
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root == None:
            return 
        self.seq.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)