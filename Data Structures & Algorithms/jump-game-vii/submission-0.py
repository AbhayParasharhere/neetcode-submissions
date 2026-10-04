class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # t i shows teh numerb of ways to reach i
        # initally t[0] = 1 as tehre is one way to reach 0 which is excatly itself
        # as we move the numerb of ways in our window increases and decreases accordingly
        n = len(s)
        t = [0] * n
        t[0] = 1
        count = 0

        for i in range(1,n):
            # look into our window range we add teh numebr just reached into our window and increas e count apporpirately
            if i - minJump >= 0:
                count += t[i - minJump]
            # thsi leaves our window
            if i - maxJump - 1 >= 0:
                count -= t[i - maxJump - 1]
            
            if s[i] == '0':
                t[i] = 1 if count > 0 else 0
        
        return t[n-1] > 0