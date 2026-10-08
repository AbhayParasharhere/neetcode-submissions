class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # a deque to track the smallest element left sa swe will need it
        q = deque()
        n = len(hand)

        if n % groupSize != 0:      # <-- ADD THIS
            return False
        hand_asc = sorted(hand)
        hmap = Counter(hand)
        q.append(hand_asc[0])
        i = 1
        while i < n:
            # skip dups excpet first instace
            while i < n and hand_asc[i-1] == hand_asc[i]:
                i += 1
            if i < n: # Guard against walking off the array
                q.append(hand_asc[i])
            i += 1
        
        # q  stat tracks the smallest left always
        need = q[0]
        cur_group = 0
        marked = 0

        while marked < n:
            
            # we get the need size into the array 
            # print(need,cur_group)
            if need not in hmap:
                # print('not',need,cur_group)
                return False
            hmap[need] -= 1
            cur_group += 1
            marked += 1
            if hmap[need] == 0:
                if q and q[0] == need:
                    q.popleft()
                del hmap[need]
            need += 1
            if cur_group == groupSize:
                if q:
                    need = q[0]
                cur_group = 0
        return marked == n


        
            