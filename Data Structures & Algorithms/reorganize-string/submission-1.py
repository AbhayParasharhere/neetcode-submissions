import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        # create a freq map
        # then greddily try to finish the one with the highest freq count first
        # if cur char same as top of heap then pop it get the next one before moving push the one u popped

        hmap = Counter(s)
        
        # create heap by freq
        hp = [(count,ch) for ch,count in hmap.items()]
        heapq.heapify_max(hp)
        
        res = []
        while hp:
            cur_char = res[-1] if res else ""
            popped_temp = None
            if hp[0][1] == cur_char:
                # only the repeating char with what we have is left
                # impossible to build without repeat
                if len(hp) == 1:
                    return ""
                popped_temp = heapq.heappop_max(hp)
            to_add_u,to_add_ch = heapq.heappop_max(hp)
            to_add_u -= 1
            # push leftover
            if to_add_u > 0:
                heapq.heappush_max(hp,(to_add_u,to_add_ch))
            if popped_temp is not None:
                heapq.heappush_max(hp,popped_temp)
            res.append(to_add_ch)
        return "".join(res)
