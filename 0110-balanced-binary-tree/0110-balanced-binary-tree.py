# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Bottom-Up 방식
    def check_height(self, root):
        if not root:
            return 0

        # 루트를 기준으로 왼쪽 서브트리와 오른쪽 서브트리의 height를 각각 확인
        left = self.check_height(root.left)
        right = self.check_height(root.right)

        # 왼쪽, 오른쪽 서브트리의 균형이 안 맞을 경우
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        # 왼쪽, 오른쪽 서브트리 중 높은 height + 1을 root의 height로 리턴
        return max(left, right) + 1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_height(root) != -1
        