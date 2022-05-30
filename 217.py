def contains_duplicate(nums):
    hash_table=set()
    for num in nums:
        if num in hash_table:
            return True
        hash_table.add(num)
    return False