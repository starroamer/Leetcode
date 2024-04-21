from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeUitl:
    @staticmethod
    def makeBinaryTree(vals):
        root = None
        if not vals or vals[0] == "null":
            return root
        root_val = vals.pop(0)
        root = TreeNode(val=root_val)
        node_list = [root]
        while node_list and vals:
            node = node_list.pop(0)
            if vals:
                left_val = vals.pop(0)
                if left_val != "null":
                    left_leaf = TreeNode(left_val)
                    node.left = left_leaf
                    node_list.append(left_leaf)
            if vals:
                right_val = vals.pop(0)
                if right_val != "null":
                    right_leaf = TreeNode(right_val)
                    node.right = right_leaf
                    node_list.append(right_leaf)

        return root
