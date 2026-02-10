class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = left + 1
        max_len = 1
        
        cur_len = 1

        if len(s) < 1:
            return 0
        cur_pattern = s[0]

        while left < right and right < len(s):
            
            if s[left] != s[right] and s[right] not in cur_pattern:
                cur_len+=1
                cur_pattern+=s[right]
                right+=1
                max_len = max(max_len, cur_len)
            else:
                left+=1
                right= left + 1
                cur_pattern = s[left]
                cur_len = 1
        return max_len
            
        