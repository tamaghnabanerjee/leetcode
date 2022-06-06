'''
33. Search in Rotated Sorted Array (Medium)
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''
def search_rotated_sorted_array(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if target==nums[mid]:
            return mid
        if nums[mid]>=nums[l]:
            if target<nums[l] or target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        else:
            if target>nums[r] or target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
    return -1

if __name__=='__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search_rotated_sorted_array(nums,target))