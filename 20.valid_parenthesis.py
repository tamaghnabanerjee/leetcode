'''
20. Valid Parentheses (Easy)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 2:
Input: s = "()[]{}"
Output: true
'''
def paranthesis_checker(s):
    hash_map={ ')' : '(' , ']' : '[', '}' :  '{'}
    stack=[]
    for c in s:
        if c in hash_map and len(stack)!=0 and hash_map[c]==stack[-1]:
                stack.pop()
        else:
            stack.append(c)
    return len(stack)==0

if __name__=='__main__':
    s="()[]{}"
    print(paranthesis_checker(s))
