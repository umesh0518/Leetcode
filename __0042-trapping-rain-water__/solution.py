class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        leftMax = height[left]
        rightMax = height[right]

        water = 0

        while left < right:

            """
            check which side is bigger, then we chose the smaller size as it will be the side that leaks

            if leftmax < rightmax , we know left side will leak and dont worry about right side

            so we check height[left], and height[left+1] and chose max
            and if 
            if left+1 was max and cureent( left +1 ) same we wont trap anything
            if left( was max) and left + 1 is small so we have dip and it will trap


            same thing for right :
            right -1 dips we trap between right , right -1 else no trapping

            """

            if leftMax < rightMax:
                left+=1
                leftMax = max(leftMax, height[left])
                water+= leftMax - height[left]
            
            else:
                right-=1
                rightMax = max(rightMax, height[right])
                water+= rightMax - height[right]
        return water