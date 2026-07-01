class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        n = len(s2)
        s1Map = Counter(s1)
        win = {}
        winLen = len(s1)

        for r in range(n):
            # put in window
            win[s2[r]] = win.get(s2[r],0) + 1

            # shrink condition
            if r - l + 1 > winLen:
                ch2remove = s2[l]
                win[ch2remove] -= 1
                if win[ch2remove] <= 0: del win[ch2remove]
                l += 1
            if r - l + 1 == winLen:
                if win == s1Map: return True
        return False