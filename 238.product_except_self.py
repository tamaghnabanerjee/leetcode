'''
238. Product of Array Except Self (Medium)
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''
# Division method
def product_except_self(nums):
    product=1
    answer=[]
    for i in range(len(nums)):
        product*=nums[i]
    for num in nums:
        answer.append(product//num)
    return answer
# Without division approach
def prodduct_except_self_method2(nums):
    answer=[]
    product=1
    for i in range(len(nums)):
        product*=nums[i]
        answer.append(product)
    post=1
    for j in range(len(nums)-1,-1,-1):
        if j>0:
            answer[j]=answer[j-1]*post
            post*=nums[j]
    answer[0]=post
    return answer


if __name__=='__main__':
    nums=[1,2,3,4]
    print(prodduct_except_self_method2(nums))
    