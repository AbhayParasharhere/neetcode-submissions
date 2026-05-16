class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        l = 0
        r = len(people) - 1
        res = 0

        while l <= r:
            # Send the most heavy with teh most lighest pair
            # if tehir sum is more than the llimit - just send the heaviest
            sum = people[l] + people[r]
            if sum <= limit:
                r -= 1
                l += 1
                res += 1
            else:
                r -= 1
                res += 1
        return res



        

