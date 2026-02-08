class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        max_area = 0
        stack = [] # pair of index and height

        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                indx, h = stack.pop()
                max_area = max(max_area, h * (i - indx))
                start = indx  # we now start from the index we poped and move right again or see if we can pop again

            # if greater than = failes that means curr value is greater than last so add to stack.
            stack.append([start,heights[i]])

        # for case when we never saw anything that is small and height kept on increasing so we need to calcuate area for that.
        for i, h in stack:
            max_area = max(max_area, h * (n-i))

        return max_area