class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        winLen = len(s1)
        n = len(s2)
        l = 0
        s1map = [0 for _ in range(26)]

        for i in range(len(s1)):
            idx = ord(s1[i]) - ord('a')
            s1map[idx] += 1

        hmap = [0 for _ in range(26)]

        # window fixed size of winLen
        # compare when window reaches this point if equal to s1map return True

        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')
            hmap[idx] += 1
            if r - l + 1 > winLen:
                # remove the char at l
                idx2remove = ord(s2[l]) - ord('a')
                hmap[idx2remove] -= 1
                l += 1

            if r - l + 1 == winLen:
            #     # Compare if this window is same as s1map
                if s1map == hmap:
                    return True
        return False

            


            
