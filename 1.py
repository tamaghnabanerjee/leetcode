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