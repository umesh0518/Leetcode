class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - 2 # so left is 2nd last and right is last
        

        while pivot >=0 and nums[pivot] >= nums[pivot + 1]:
            pivot-=1
        
        if pivot >= 0:
            sucessor = len(nums) - 1 # start from end right and come until pivot to find successor which shoudl be smallest( not just equal)

            while nums[sucessor] <= nums[pivot]:
                sucessor-=1
            
            #python way of replacing:
            nums[pivot], nums[sucessor] =  nums[sucessor], nums[pivot]

        #else part pivot was at -1 now evertying on the right of pivot needs to be in smallest to largetst order
        start = pivot + 1 # -1 so bring to 0
        end = len(nums) -1 

        while start < end:
            #easy reversal:
            nums[start], nums[end] =  nums[end], nums[start]
            start+=1
            end-=1




        