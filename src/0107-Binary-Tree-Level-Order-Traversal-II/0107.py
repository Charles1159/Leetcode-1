# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, result = [root], []
        while any(q):
            tmp = list()
            len_q = len(q)
            for _ in range(len_q):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.insert(0, tmp)
        return result

def createTree(root):
    if root == None:
        return root

    Root = TreeNode(root[0])
    nodeQueue = [Root]
    index = 1
    front = 0
    while index < len(root):
        node = nodeQueue[front]
        
        item = root[index]
        index += 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(root):
            break

        item = root[index]
        index += 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
        
        front += 1

    return Root

def printTree(root):
    if root != None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)      

if __name__ == "__main__":
    root = [1,None,2,3]
    treeRoot = createTree(root)
    printTree(treeRoot)
    print(Solution().levelOrderBottom(treeRoot))