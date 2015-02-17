# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        
        if root != None:
            if root.left == None and root.right == None and sum == root.val:
                    return True
            l = self.hasPathSum(root.left, sum - root.val)
            r = self.hasPathSum(root.right, sum - root.val)
            return r or l
            
        return False
