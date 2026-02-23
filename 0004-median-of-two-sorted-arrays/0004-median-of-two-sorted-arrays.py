
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        combined.sort()

        N = len(combined)

        if N % 2 == 0:
            l = int(N//2) -1 
            r = l+ 1
            sum = combined[l] + combined[r]
            m = sum/2
            return (m)


        else:
            c = int(((N + 1)/2)-1)
            return combined[c]


        