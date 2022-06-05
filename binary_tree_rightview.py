'''
199. Binary Tree Right Side View (Medium)
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
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
    
    def right_side_view(self):
        if not self.root: return []
        curr=self.root
        result=[]
        q=[]
        q.append(curr)
        right_node=None
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                if node is not None:
                    right_node=node
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
            result.append(right_node.data)
        return result
    

if __name__=='__main__':
    tree=Tree(4)
    tree.insert(0)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(6)
    tree.insert(7)
    tree.insert(9)
    print(tree.right_side_view())
    