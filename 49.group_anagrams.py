'''49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
def group_anagrams(strs):
    anagrams_map={}
    for s in strs:
        strng=''.join(sorted(s))
        if strng not in anagrams_map:
            anagrams_map[strng]=[s]
        else:
            anagrams_map[strng].append(s)
    return [v for v in anagrams_map.values()]

if __name__=='__main__':
    strs=["eat","tea","tan","ate","nat","bat","ant"]
    print(group_anagrams(strs))
    
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Naive solution: O(n^2)
'''
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_map={}
    anagrams=[]
    anagrams_set=set()
    result=[]
    for i in range(len(strs)):
        if strs[i] not in anagrams_set:
            anagrams_set.add(strs[i])
            anagrams=[strs[i]]
            for j in range(i+1,len(strs)):
                if self.is_anagram(strs[i],strs[j]):
                    anagrams.append(strs[j])
                    anagrams_set.add(strs[j])
            anagram_map[strs[i]]=anagrams
    for v in anagram_map.values():
        result.append(v)
    return result
    
def is_anagram(self,str1,str2):
    if len(str1)!=len(str2):
        return False
    map1={}
    map2={}
    for i in range(len(str1)):
        map1[str1[i]]=1+map1.get(str1[i],0)
        map2[str2[i]]=1+map2.get(str2[i],0)
    for k in str1:
        if map1[k]!=map2.get(k,0):
            return False
    return True
'''