class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right)//2
            if nums[mid]== target:
                return mid

            #check which side is smoot, since no duplicate so 
            if nums[left] <= nums[mid]:
                #left side is sorted and smooth
                #check left <= target < mid to see if target is there
                if nums[left] <= target and target < nums[mid]:
                    right = mid -1
                else:
                    #target was on righht side so move left to mid
                    left = mid + 1
            else:
                # right side was smooth and sorted
                #check mid < target <= right ( shoud b)
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    #even though this was smooth side target is in left side
                    right = mid -1
        return -1




