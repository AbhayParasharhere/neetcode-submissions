class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # shrink when the window length is equal to the length of s1
        m = len(s1)
        # calculate the result 
        win = {}
        s1map = dict(Counter(s1))
        n = len(s2)
        l = 0

        for r in range(n):
            # put char in win
            ch = s2[r]
            win[ch] = win.get(ch,0) + 1

            if r - l + 1 > m:
                # slide
                ch2remove = s2[l]
                win[ch2remove] -= 1
                if win[ch2remove] <= 0: del win[ch2remove]
                l += 1            
            # calculate the res
            if win == s1map: return True
        
        return False

