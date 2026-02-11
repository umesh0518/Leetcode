class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        residueLen=0

        for i, c in enumerate(s):
            seen.add(c)
            curLen = i+1
            check = curLen % 3

            if len(seen) == check:
                residueLen+=1
        return residueLen