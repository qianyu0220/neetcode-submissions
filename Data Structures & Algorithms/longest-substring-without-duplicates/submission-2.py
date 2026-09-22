class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        output = 0
        l = 0
        charset = set()
        for r in range(n):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            output = max(output, r-l+1)
        return output
