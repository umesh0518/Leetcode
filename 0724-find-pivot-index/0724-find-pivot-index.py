class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)

        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i] # total - left sum - current number = right sum at that index

            #check if now right sum == left sum 
            if left_sum == right_sum:
                return i # pivot found
            
            left_sum += nums[i]
        
        return -1


        