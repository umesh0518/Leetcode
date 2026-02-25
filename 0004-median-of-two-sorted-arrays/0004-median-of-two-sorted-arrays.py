import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # so always smaller is A
        if len(A) > len(B):
            A, B = B, A
        
        left, right = 0, len(A)-1

        while True:

            pivotA = (left + right )//2
            pivotB = half - pivotA - 2


            Aleft = A[pivotA] if pivotA>=0 else float("-infinity")
            Aright = A[pivotA + 1] if (pivotA + 1) < len(A) else float("infinity")

            Bleft = B[pivotB] if pivotB >= 0 else float("-infinity")
            Bright = B[pivotB + 1] if (pivotB + 1) < len(B) else float("infinity")


            if Aleft <=Bright and Bleft <= Aright:
                #means breaking pivot points are correct

                if total % 2: 
                    #odd case so just return the minimum between Aright and Bright
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright:
                #means left of A was still bigger, 
                right = pivotA - 1
            else:
                left = pivotA + 1
