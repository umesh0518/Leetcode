class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevSeen = {}
        for i, n in enumerate(numbers):
            diff = target -n
            if diff in prevSeen:
                return[prevSeen[diff],i+1]
            prevSeen[n] = i+1
        return []
