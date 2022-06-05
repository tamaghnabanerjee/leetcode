'''
100. Same Tree (Easy)
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
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
    
def is_same_tree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.data!=q.data:
        return False
    return is_same_tree(p.left,q.left) and is_same_tree(p.right,q.right)


if __name__=='__main__':
    tree1=Tree(4)
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(5)
    tree1.insert(6)
    
    tree2=Tree(4)
    tree2.insert(9)
    tree2.insert(2)
    tree2.insert(5)
    tree2.insert(6)

    p=tree1.root
    q=tree2.root
    print(is_same_tree(p,q))