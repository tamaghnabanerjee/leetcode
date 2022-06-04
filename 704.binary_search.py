'''
704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''
# recursive
def search_recursive(nums,target):
    def binary_search(low,high):
        if low>high:
            return -1
        mid=(low+high)//2
        if target==nums[mid]:
            return mid
        elif target<nums[mid]:
            return binary_search(low,mid-1)
        elif target>nums[mid]:
            return binary_search(mid+1,high)
    return binary_search(0,len(nums)-1)

# iterative
def search_iterative(nums,target):
    def binary_search(l,r):
        while l<=r:
            m=(l+r)//2
            if target==nums[m]:
                return m
            if target<nums[m]:
                r=m-1
            elif target>nums[m]:
                l=m+1
        return -1
    return binary_search(0,len(nums)-1)
            
        

if __name__=='__main__':
    # nums=[-1,0,3,5,9,12]
    # len(nums)-1=5
    nums=[5]
    target=5
    print(search_iterative(nums,target))
