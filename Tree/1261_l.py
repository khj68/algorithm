# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.root = root
        self.exist = set()
        def clean(node):
            self.exist.add(node.val)
            if node.left:
                node.left.val = node.val*2 + 1
                clean(node.left)
            if node.right:
                node.right.val = node.val*2 + 2
                clean(node.right)
        clean(root)
    def find(self, target: int) -> bool:
        return target in self.exist


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)