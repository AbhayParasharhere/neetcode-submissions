class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to alpahnumeric
        l = 0
        r = len(s) - 1

        while l < r and l < len(s) and r > 0:
            while s[l].isalnum() == False:
                l += 1
                if l > len(s) - 1:
                    break
            while s[r].isalnum() == False:
                r -= 1
                if r < 0:
                    break
            if r >= 0 and l < len(s) - 1 and s[l].lower() != s[r].lower():
                # print(s[l],s[r])
                return False
            l += 1
            r -= 1
        return True

