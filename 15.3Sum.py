'''
15. 3Sum (Medium)
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
 Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''
def three_sum(nums):
    target=0
    result=[]
    nums.sort()
    # [-4,-1,-1,0,1,2]
    for i in range(len(nums)):
        # handling duplicates for the pivot 3sum
        if i>0 and nums[i-1]==nums[i]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            target=nums[l]+nums[r]+nums[i]
            if target<0:
                l+=1
            elif target>0:
                r-=1
            else:
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                # handling duplicates within 2sum
                while l<r and nums[l]==nums[l-1]:
                    l+=1
    return result

if __name__=='__main__':
    nums=[-1,0,1,2,-1,-4]
    print(three_sum(nums))
