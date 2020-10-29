# Leetcode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/ 

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val  # 表示本节点的值、字符、数字或者其他类型都可以，在定义本节点时传入
#         self.left = left  # 表示本节点的左子节点，可以为空或节点，初始值为None
#         self.right = right  # 表示本节点的子节点，可以为空或节点，初始值为None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Method1(faster than 15.27%, 60ms): 前序遍历: 先根，后左节点，再右节点
        def preorder_traversal(root):
            li = []
            if root == None:
                return []
            else:
                li += [root.val]
                li += preorder_traversal(root.left)   # 不能加[]，否则会变成list of list
                li += preorder_traversal(root.right)
            return li
        
        # 需要排序
        val_list = preorder_traversal(root)
        val_list.sort()
        return val_list[k-1]
    
    
    
    
        # Method3(faster than 70%, 44ms): 中序遍历: 先左节点，再根，再右节点
        # 因此中序遍历一定是由小及大的，不用排序了
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val]  + inorder(root.right)
        
        ans = inorder(root)
        return ans[k-1]

        