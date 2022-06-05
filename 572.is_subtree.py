'''
572. Subtree of Another Tree (Easy)
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self,value):
        self.root=Node(value)
    
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

def is_subtree(root1,root2):
    if root2==None:
        return True
    if root1==None:
        return False
    if is_same_tree(root1,root2):
        return True
    return is_subtree(root1.left,root2) or is_subtree(root1.right,root2)

def is_same_tree(root1,root2):
    if root1==None and root2==None:
        return True
    if root1 and root2 and root1.data==root2.data:
        return is_same_tree(root1.left,root2.left) and is_same_tree(root1.right,root2.right)
    return False

if __name__=='__main__':
    tree1=Tree(4)
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(5)
    tree1.insert(6)
    
    tree2=Tree(4)
    tree2.insert(1)
    tree2.insert(2)
    tree2.insert(5)
    tree2.insert(6)

    p=tree1.root
    q=tree2.root
    print(is_subtree(p,q))