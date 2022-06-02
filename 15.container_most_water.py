'''
11. Container With Most Water (Medium)
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container. 
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

def container_most_water(height):
    l=0
    r=len(height)-1
    max_area=0
    while l<r:
        area=min(height[l],height[r])*(r-l)
        if area>max_area:
            max_area=area
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return max_area

if __name__=='__main__':
    height=[1,8,6,2,5,4,8,3,7]
    print(container_most_water(height))