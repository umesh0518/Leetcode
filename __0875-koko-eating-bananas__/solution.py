class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)

        res = right

        while left <= right:

            mid_rate = (left + right)//2

            total_hr = 0
            for p in piles:
                total_hr += math.ceil(p/mid_rate)
            
            if total_hr <= h:
                #means rate was fast we can go slow:
                right = mid_rate - 1
                res = mid_rate # so far best rate
            else:
                # we went too slow so increase the rate
                left = mid_rate + 1
        return res


