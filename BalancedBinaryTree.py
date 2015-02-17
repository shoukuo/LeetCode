# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        self.addDeep(root)
        return self.testBalanced(root)
        
    def testBalanced(self, root):
        if root == None:
            return True
        tl = self.testBalanced(root.left)
        tr = self.testBalanced(root.right)
        return tl == True and tr == True and abs(root.left.val-root.right.val) < 2
        
    def addDeep(self, root):
        if root != None:
            dl = self.addDeep(root.left)
            dr = self.addDeep(root.right)
            root.val = max(dl, dr) + 1
            return root.val
        return 0
        