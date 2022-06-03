'''
424. Longest Repeating Character Replacement (Medium)
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase 
English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''
def longest_repeating_chars_replacement(s,k):
    l=0
    hash_map={}
    max_length=0
    for r in range(len(s)):
        hash_map[s[r]]=1+hash_map.get(s[r],0)
        while (r-l+1)-max(hash_map.values())>k:
            hash_map[s[l]]-=1
            l+=1
        max_length=max((r-l+1),max_length)
    return max_length


if __name__=='__main__':
    s="AABABBA"
    k=1
    print(longest_repeating_chars_replacement(s,k))