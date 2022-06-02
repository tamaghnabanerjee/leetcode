'''
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''
def trap_rain_water(height):
    # Brute Force
    # max_left=[0]*len(height)
    # max_right=[0]*len(height)
    # min_LR=[0]*len(height)
    # for i in range(1,len(height)):
    #     max_left[i]=max(height[:i])
    # max_left[0]=0
    # for i in range(len(height)-2,-1,-1):
    #     max_right[i]=max(height[i+1:])
    # max_right[len(height)-1]=0
    # for i in range(len(height)):
    #     min_LR[i]=min(max_left[i],max_right[i])

    # result=0        
    # for i in range(len(height)):
    #     target=min_LR[i]-height[i]
    #     if target<0:
    #         target=0
    #     result+=target
    # return result
    if not height:
        return 0
    l=0
    r=len(height)-1
    result=0
    l_max=height[l]
    r_max=height[r]
    while l<r:
        if l_max<r_max:
            l+=1
            l_max=max(l_max,height[l])
            result+=l_max-height[l]
        else:
            r-=1
            r_max=max(r_max,height[r])
            result+=r_max-height[r]
    return result


if __name__=='__main__':
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap_rain_water(height))