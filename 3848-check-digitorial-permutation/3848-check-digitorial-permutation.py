class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        s = str(n)
        n = len(s) -1 
        fs = 0
        
        for x in s:
            print("x = ", x)
            fs+= math.factorial(int(x))
        return sorted(s) == sorted(str(fs))
        
            
        