class Solution:
    def countMonobit(self, n: int) -> int:
        c = 1
        bit_rep = 1
        while bit_rep <=n:
            c+=1
            bit_rep = bit_rep << 1 | 1
        return c