"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs create new node during push time
        # in q push a tuple containing both original and address copy as we need tehm hand by hand
        # as original neighbour are put as copy neighbours when we loop into neighbour we create them as well
        if not node: return None
        q = deque()
        visited = set()

        # push first node but create its copy as well to push into q
        # mark node as visited
        cnode = Node(node.val)
        q.append((node,cnode))
        visited.add(node)
        # for visisted neighbors thata re already creatd we can use a map to push them
        # mapping node to copy nodes
        hmap = {
            node:cnode
        }
        while q:
            u,cu = q.popleft()

            for v in u.neighbors:
                # only for unvisited v's
                if v not in visited:
                    visited.add(v)
                    # create copy v
                    cv = Node(v.val)
                    # push copy into cu neighbours
                    cu.neighbors.append(cv)
                    # update into hmap
                    hmap[v] = cv
                    # push into q for continued traversal
                    q.append((v,cv))
                else:
                    cu.neighbors.append(hmap[v])
        return cnode



