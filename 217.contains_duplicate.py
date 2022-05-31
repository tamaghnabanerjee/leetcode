'''217. Contains Duplicate (Easy)
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
'''

def contains_duplicate(nums):
    hash_table=set()
    for num in nums:
        if num in hash_table:
            return True
        hash_table.add(num)
    return False

if __name__=='__main__':
    nums = [1,2,3,1]
    print(contains_duplicate(nums))