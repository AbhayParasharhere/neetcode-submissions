from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # from all our bills received we give the largest bill first 
        # why cos then we can combine our smaller for amount laregr also makes so that leaves mroe options for smaller as well as same laregr. bilsl for us

        if bills[0] != 5: return False
        hmap = defaultdict(int)
        hmap[5] = 1
        
        for i in range(1,len(bills)):
            amt = bills[i]
            if amt == 5:
                hmap[5] += 1
            else:
                # need to give change
                hmap[amt] += 1
                if amt == 10:
                    # need to return a 5 dollar bill
                    if hmap[5] <= 0:
                        return False
                    hmap[5] -= 1
                elif amt == 20:
                    # greedily chosoe 10 first - return 15 back
                    if hmap[10] > 0:
                        hmap[10] -= 1
                        if hmap[5] <= 0:
                            return False
                        hmap[5] -= 1
                    else:
                        if hmap[5] < 3:
                            return False
                        hmap[5] -= 3
        return True