'''
21. Merge Two Sorted Lists (Easy)
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        
    def insert(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            node=Node(value)
            self.tail.next=node
            self.tail=node
        return self.head  
            
    def print_list(self):
        if self.head==None:
            return None
        curr=self.head
        while curr:
            print(curr.value)
            curr=curr.next
            
class MergeLists:
    def __init__(self):
        self.merged_list=LinkedList(None)
        
    def merge(self,list1,list2):
        if list1==None or list2==None:
            return None
        curr=self.merged_list.head
        curr1=list1.head
        curr2=list2.head
        while curr1 and curr2:
            if curr1.value<=curr2.value:
                curr.next=curr1
                curr1=curr1.next
            else:
                curr.next=curr2
                curr2=curr2.next
            curr=curr.next
        if curr1:
            curr.next=curr1
        if curr2:
            curr.next=curr2
        self.merged_list.head=self.merged_list.head.next
    
    def print_list(self):
        curr=self.merged_list.head
        while curr:
            print(curr.value)
            curr=curr.next
    
if __name__=='__main__':
    list1=LinkedList(10)
    list2=LinkedList(20)
    list1.insert(30)
    list1.insert(50)
    list2.insert(40)
    list2.insert(60)
    list_final=MergeLists()
    list_final.merge(None,None)
    list_final.print_list()
 
    