'''74. Search a 2D Matrix
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''
def search_matrix(matrix,target):
    def element_search(nums,l,r):
        while l<=r:
            m=(l+r)//2
            if target<nums[m]:
                r=m-1
            elif target>nums[m]:
                l=m+1
            else:
                return True
        return False
    
    def row_search(matrix):
        l=0
        r=len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if target<matrix[m][0]:
                r=m-1
            elif target>matrix[m][-1]:
                l=m+1
            else:
                return m
        return None
    if row_search(matrix):
        return False
    else:
        nums=matrix[row_search(matrix)]
        return element_search(nums,0,len(nums)-1)
    
    

if __name__=='__main__':
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target=3
    print(search_matrix(matrix,target))