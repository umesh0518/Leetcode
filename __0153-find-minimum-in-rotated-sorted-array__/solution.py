class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n -1 

        while left < right:
            """
            mid = left + ( right - left) //2 # is actually worse in python
            """
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                # mid was still in potential solutions so keep it
                right = mid
            else:
                left = mid + 1 # mid was big can throw it
        return nums[left]

