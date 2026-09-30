class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxL = 0
        l, r = 0, 1
        setS = set()
        while r < n:
            setS.add(s[l])
            if s[r] in setS:
                length = r-l
                maxL = max(maxL, length)
                l = r
            else:
                setS.add(s[r])
            r += 1
        return maxL
