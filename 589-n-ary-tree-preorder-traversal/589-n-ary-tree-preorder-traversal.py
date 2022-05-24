"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def solve(root, res):
            if root:
                res.append(root.val)

                for child in root.children:
                    solve(child, res)
            return res
        return solve(root, [])