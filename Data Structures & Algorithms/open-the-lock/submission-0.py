class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # looks like dp but not dp cos we can techinally go back toa c hoice we made earleir so not a DAG
        # so graph is a vaid option
        # say we are at arbitary position abcd then instead of whole sequence
        # a wants to reach t1 b wants t2 and s on
        # and each move we can only rotate once of abcd to get closer to theri atregt
        # each wheel that we decide to move can go a-1 or a+1
        # minm so thinking bfs and thinig from t1t2t3t4 to 0,0,0,0
        # lets try in 2 wheels case first tehn its easy to visualize as a grid porblem from 0,0 to t1t2
        # in shortest path avoidng all teh deadends 
        # damn i can see it in the 2 lock case goddamn it a trick question indeed

        # lets see the movement of neighborus in a 4d grid then
        # in 2d grid its 4 directions in 3d its 8 so 4d its 16 neighbours or 16 moves in each grid cell
        hmap = set()

        for deadend in deadends:
            hmap.add(deadend)
        if "0000" in hmap:return -1
        neighbours = []
        for move in (-1, 1):
            neighbours.append((move, 0, 0, 0))
            neighbours.append((0, move, 0, 0))
            neighbours.append((0, 0, move, 0))
            neighbours.append((0, 0, 0, move))

        # distance from source 0000 to itself is 0
        # we use visted array instead of djikstra and teh max level our q reaches is teh minm cost
        q = deque()
        visited = [[[[False for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
        q.append((0,0,0,0))
        visited[0][0][0][0] = True

        max_level = -1
        while q:
            level = len(q)
            max_level += 1
            for _ in range(level):
                ua,ub,uc,ud = q.popleft()
                if f"{ua}{ub}{uc}{ud}" == target:
                    return max_level
                for delta_a,delta_b,delta_c,delta_d in neighbours:
                    va = (delta_a + ua + 10) % 10
                    vb = (delta_b + ub + 10) % 10
                    vc = (delta_c + uc + 10) % 10
                    vd = (delta_d + ud + 10) % 10
                
                    # we cant traverse or continue through deadends or already visited cells to avoid inf loop
                    if visited[va][vb][vc][vd] or f"{va}{vb}{vc}{vd}" in hmap:
                        continue
                    # mark visited and append to Q
                    visited[va][vb][vc][vd] = True
                    q.append((va,vb,vc,vd))
    
        # print(neighbours,len(neighbours),visited)
        return -1
