def isSymmetric(self, root):
        # root.left.right.val == root.right.left.val
        # root.left.left.val == root.right.right.val
        
        def search(left, right):
            print(left.val, right.val)
            left_left = left_right = True
            if left.left:
                left_left = search(left.left, right.right)
            if left.right:
                left_right = search(left.right, right.left)
            
            return left.val == right.val and left_left and left_right
        
        return search(root.left, root.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode()
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(0, root))