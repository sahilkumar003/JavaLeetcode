# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, root1, root2, prevRoot1, left, right):
        if((root1 == None and root2 == None) or root2 == None):
            return;
        elif(root1 == None):
            node = TreeNode(val=root2.val);
            if(left == 1):
                root1 = node;
                prevRoot1.left = root1;
            else:
                root1 = node;
                prevRoot1.right = root1;
        else:
            root1.val = root1.val +  root2.val;
            
        
        self.merge(root1.left, root2.left, root1, 1, 0);
        self.merge(root1.right, root2.right, root1, 0, 1);
        
        return;
        
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root1 == None):
            return root2;
        elif(root2 == None):
            return root1;
        
        self.merge(root1, root2, None, 0, 0);
        return root1;