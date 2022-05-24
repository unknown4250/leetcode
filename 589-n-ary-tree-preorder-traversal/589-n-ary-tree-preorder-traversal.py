"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        output = []
        self.dfs(root, output)
        return output
        
    def dfs(self, root, res):
        if not root:
            return

        res.append(root.val)
        for child in root.children:
            self.dfs(child, res)