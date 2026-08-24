class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Mf = 0
        res = 0
        l = 0
        r = 0
        freq = dict()
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            Mf = max(Mf, freq[s[r]])
            windowSize = (r - l + 1) 
            if(windowSize - Mf <= k):
                res = max(res,windowSize)
            else:
                freq[s[l]] -= 1
                l+=1
            r+=1
        return res