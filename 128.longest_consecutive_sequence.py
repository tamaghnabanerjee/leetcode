'''
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
# check if -1 integer is in nums_set
# if yes then while loop to get the next ones and then length
def longest_consecutive_sequence(nums):
    nums_set=set(nums)
    max_length=0
    for i in range(len(nums)):
        if nums[i]-1 not in nums_set:
            r=0
            while nums[i]+r in nums_set:
                r+=1
            max_length=max(max_length,r)
    return max_length

if __name__=='__main__':
    nums=[100,4,200,1,3,2]
    print(longest_consecutive_sequence(nums))