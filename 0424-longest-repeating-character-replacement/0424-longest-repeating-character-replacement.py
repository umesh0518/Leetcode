class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dic = {}

        res = 0

        left = 0 
        for right in range(len(s)):
            count_dic[s[right]] = 1 + count_dic.get(s[right],0)

            while ( right - left + 1) - max ( count_dic.values()) > k:
                count_dic[s[left]]-=1
                left+=1
            res = max(res, (right - left + 1))
        return res
