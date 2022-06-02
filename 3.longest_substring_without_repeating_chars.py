'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
def longest_substr(s):
    hash_set=set()
    length=max_length=0
    l=0
    r=0
    while r<len(s):
        if s[r] in hash_set:
            length=len(hash_set)
            # removes oone-by-one upto first duplicate by incrementing l (till now r is same)
            print("removed_item",s[l])
            hash_set.remove(s[l])
            l+=1
        else:
            hash_set.add(s[r])
            length=len(hash_set)
            r+=1
        max_length=max(max_length,length)
    return max_length


if __name__=='__main__':
    s="qrsvbspk"
    print(longest_substr(s))