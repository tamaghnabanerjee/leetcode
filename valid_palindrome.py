'''
125. Valid Palindrome (Easy)
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise. 
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
def is_alpha_numeric(s):
    return ord('A')<=ord(s)<=ord('Z') \
           or ord('a')<=ord(s)<=ord('z') \
           or ord('0')<=ord(s)<=ord('9')

def is_palindrome(s):
    l=0
    r=len(s)-1
    while l<=r:
        # while l<r and not s[l].isalnum():
        while l<r and not is_alpha_numeric(s[l]):
            l+=1
        # while l<r and not s[r].isalnum():
        while l<r and not is_alpha_numeric(s[r]):
            r-=1
        if s[l].lower()!=s[r].lower():
            return False
        l+=1
        r-=1
    return True

if __name__=='__main__':
    s="A man, a plan, a canal: Panama"
    print(is_palindrome(s))