class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t) > len(s) or t == ""):
            return ""
        l = 0

        resLen = float("inf")
        have = 0
       
        res = [-1,-1]
        Tcount,window = {},{}
        for c in t :
            Tcount[c] = 1 + Tcount.get(c,0)
        need = len(Tcount) 
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if(c in Tcount and Tcount[c] == window[c]):
                have +=1
            while have == need:
                if(r - l + 1 < resLen):
                    resLen = r - l +1
                    res = [l,r]
                window[s[l]] -=1
                if(s[l] in Tcount and Tcount[s[l]] > window[s[l]]):
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen!= float("inf") else ""  

