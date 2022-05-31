'''
242. Valid Anagram (Easy)
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

'''
def is_anagram(s,t):
    if len(s)!=len(t):
        return False
    map_s={}
    map_t={}
    for i in range(len(s)):
        map_s[s[i]]=1+map_s.get(s[i],0)
        map_t[t[i]]=1+map_t.get(t[i],0)
    for k,v in map_s.items():
        if map_t[k]!=map_s.get(k,0):
            return True
    return False

