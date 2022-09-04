class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def levelOrder(root) -> list[list[int]]:
    if root:
        levellen = 1
        
        result = []
        result.append([root.val])
        
        Q = []
        Q.append(root)
        
        while root and Q :
            tmp = Q.pop(0)
            if tmp.left:
                Q.append(tmp.left)
            if tmp.right:    
                Q.append(tmp.riht)
            levellen-=1
            if levellen==0 and Q:
                result.append([Q[i].val for i in range(len(Q))])
                levellen = len(Q)
        return result
    else:
        return []


        
    
        
        
