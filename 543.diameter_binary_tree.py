'''
543. Diameter of Binary Tree (Easy)
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self,data):
        self.root=Node(data)

    def insert(self,value):
        node=Node(value)
        if self.root==None:
           self.root=node
           return self.root
        curr=self.root
        while True:
            if curr.data==node.data: return False
            if node.data<curr.data:
                if not curr.left:
                    curr.left=node
                    return True
                curr=curr.left
            elif node.data>curr.data:
                if not curr.right:
                    curr.right=node
                    return True
                curr=curr.right
            
    def dfs_inorder(self):
        result=[]
        def traverse(curr):
            if curr.left is not None:
                traverse(curr.left)
            result.append(curr.data)
            if curr.right is not None:
                traverse(curr.right)
        traverse(self.root)
        return result

    def diameter_binary_tree(self):
        def diameter(root):
            if root==None:
                return -1
            lheight=height(root.left)
            rheight=height(root.right)
            
            ldiameter=diameter(root.left)
            rdiameter=diameter(root.right)
            
            return max(lheight+rheight+2, max(ldiameter,rdiameter))
        
        def height(root):
            if root==None:
                return -1
            return 1+max(height(root.left),height(root.right))
        
        return diameter(self.root)

    def height_tree(self):
        def height(root):
            if root==None:
                return -1
            return 1+max(height(root.left),height(root.right))
        return height(self.root)
    
if __name__=='__main__':
    tree=Tree(4)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)
    tree.insert(7)
    tree.insert(9)
    # print(tree.height_tree())
    print(tree.diameter_binary_tree())
    # print(tree.dfs_inorder())