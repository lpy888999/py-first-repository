class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
        
    while root or stack:#栈和当前节点都空时，说明遍历结束

        if root:#不是叶子
            stack.append(root)
            # visit() 则是先序
            root = root.left 
        else:
            last = stack.pop()  #经过第二次就出栈
            result.append(last.val)
            root = last.right 
    return result
