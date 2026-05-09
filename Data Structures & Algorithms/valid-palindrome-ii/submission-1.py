class Solution:
    def isPalin(self,s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        chance = 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                if chance == 1:
                    # choose char at l to delete
                    withoutL = self.isPalin(s[l+1:r+1])
                    withoutR = self.isPalin(s[l:r])
                    if withoutL or withoutR:
                        return True
                    else:
                        return False
                else:
                    return False
            l += 1
            r -= 1
        return True