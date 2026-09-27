class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""

        # create a heap out of a,b,c to pick the highest every time
        mp = {'a':a,'b':b,'c':c}
        hp = [(freq,ch) for ch,freq in mp.items() if freq > 0]
        heapq.heapify_max(hp)

        chSame = None
        while hp:
            popped = None
            chSame = res[-1] == res[-2] if len(res) >= 2 else None
            if chSame and hp[0][1] == res[-1]:
                # now we must reset the heap top to some otehr char
                popped = heapq.heappop_max(hp)
                # nothing left only the same ch
                if len(hp) == 0:
                    return res
            
            to_add_v,to_add_ch = heapq.heappop_max(hp)
            res += to_add_ch
            if to_add_v - 1 > 0:
                heapq.heappush_max(hp,(to_add_v - 1,to_add_ch))
            if popped:
                heapq.heappush_max(hp,popped)
        return res

