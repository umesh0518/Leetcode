class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        setnums = set(nums)

        seen = { v: 0 for v in setnums}

        for n in nums:
            seen[n] +=1

        #make a list of the value and then change to set and check for len??
        ans = [v for v in seen.values()]

        # find frequency of each value now 
        f_dict = {}
        for a in ans:
            if a in f_dict:
                f_dict[a]+=1
            else:
                f_dict[a] = 1

        for n in nums:
            num_freq = seen[n]
            if f_dict[num_freq] == 1:
                return n
        return -1
            
