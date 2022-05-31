'''
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''


def sum_nums(nums,target):
    hash_map={}
    for i in range(len(nums)):
        if target-nums[i] in hash_map:
            return [i,hash_map[target-nums[i]]]
        else:
            hash_map[nums[i]]=i


if __name__=='__main__':
    nums=[1,2,3,4,5,6]
    target=11
    print(sum_nums(nums,target))