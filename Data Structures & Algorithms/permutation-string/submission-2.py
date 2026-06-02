class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = Counter(s1)

        # fixed size sliding window of size max s1 
        # if it contains it it must match the size and match the amp exactly

        temp = {}
        k = len(s1)
        n = len(s2)
        l = 0

        for r in range(n):
            ch = s2[r]
            if ch in temp:
                temp[ch] += 1
            else:
                temp[ch] = 1
            

            if r - l + 1 > k:
                ch2remove = s2[l]
                temp[ch2remove] -= 1
                if temp[ch2remove] <= 0: temp.pop(ch2remove)
                l += 1
            if r-l + 1 == k and temp == s1Map:
                return True
        return False