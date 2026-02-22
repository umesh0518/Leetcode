class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player = True
        p1 = 0
        p2 = 0

        for i ,n in enumerate(nums):
            if n % 2 != 0:
                player = not player
            if (i + 1) % 6 == 0:
                player = not player
            if player:
                p1+=n
            else:
                p2+=n
        return p1 - p2
        