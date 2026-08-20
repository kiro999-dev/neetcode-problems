class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        if(len(s) == 0):
            return 0
        mymap = set()
        res = 1
        while  r < len(s):
            while(s[r] in mymap):
                mymap.remove(s[l])
                l = l+1
            mymap.add(s[r])
            res = max(res,(r - l) +1)
            r = r +1
        return res


        