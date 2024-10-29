# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        mpp = {val: index for index, val in enumerate(inorder)}
        
        def helper(preorder, prestart, preend, inorder, instart, inend, mpp):
            if prestart > preend or instart > inend:
                return None
            root_val = preorder[prestart]
            root = TreeNode(root_val)
            inroot = mpp[root_val]
            lhs = inroot - instart
            root.left = helper(preorder, prestart + 1, prestart + lhs, inorder, instart, inroot - 1, mpp)
            root.right = helper(preorder, prestart + lhs + 1, preend, inorder, inroot + 1, inend, mpp)
            
            return root
        return helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, mpp)
