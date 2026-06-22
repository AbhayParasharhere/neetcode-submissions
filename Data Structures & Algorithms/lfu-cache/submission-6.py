class DLL:
    def __init__(self,key,val,freq,prev=None,next=None):
        self.key, self.val, self.freq = key, val,freq
        self.prev = prev
        self.next = next

# this wrapper is put as a val in fmap used to contain a dll class at a freq
class DLLWrapper:
    def __init__(self):
        self.front = DLL(0,0,0)
        self.back = DLL(0,0,0)
        # create link
        self.front.next = self.back
        self.back.prev = self.front

class LFUCache:

    def __init__(self, capacity: int):
        # the main idea and needs for our structure
        # is that recently modified should be pushed to the front of the Q like datastructure
        # but we also maintain a hmap of frequency to their dll
        # these dll are like lru
        # but maintaing a hmap of frequency allows us to know which nodes are stiing at the same freq levek
        # then we can do a promotion level through dll ds in o1 and deletion in o1, and new node can be bundled in the correct dll in o1
        self.capacity = capacity
        self.size = 0
        self.fmap = {}
        self.minf = None
        # hmap maps the key to the node address, which we can use to promote that node to a higehr freq
        # and node itself can be used to store freq and access its dll class memebers as well
        self.hmap = {}

    def remove_node(self,node):
        # get its prev and next to remove it from chain
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def put_node(self,node,freq):         
        # put the node to the new f leevl
        if not freq in self.fmap:
            self.fmap[freq] = DLLWrapper()

        # put the node at the corresponding freq level
        # puts its just below the bak of that freq level specified
        back = self.fmap[freq].back
        prev_back = back.prev

        # stich to back
        node.next = back
        back.prev = node
    
        # stich to back prev
        prev_back.next = node
        node.prev = prev_back

    def update_min(self,prev_f):
        if prev_f == self.minf:
            # check if it only has one element after removal
            min_node = self.fmap[self.minf]
            if min_node.front.next == min_node.back:
                # its empty
                del self.fmap[self.minf]
                self.minf += 1

    # touch fx gets the corresponding node, increases its freq by 1 and its class DLL
    # by removing it from current class and also takes care of min f if it is affected
    def touch(self,node):
        prev_f = node.freq
        new_f = prev_f + 1

        # update node freq
        node.freq = new_f
        self.remove_node(node)

        # handles min udpate and hmap deletion if necessory
        self.update_min(prev_f)

        self.put_node(node,new_f)


    def get(self, key: int) -> int:
        if key not in self.hmap: return -1

        node = self.hmap[key]
        self.touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            # update the pos in dll by touch
            self.touch(node)
            return

        if self.size >= self.capacity:
            # remove the one from the fornt at the min f leevl
            node2remove = self.fmap[self.minf].front.next
            self.remove_node(node2remove)
            if node2remove.freq == self.minf:
                # handles min udpate and hmap deletion if necessory
                self.update_min(node2remove.freq)
            del self.hmap[node2remove.key]
            # clean up the hmap
            self.size -= 1
        self.size += 1
        freq = 1
        node = DLL(key,value,freq)
        # updaet hmap and minf and put back in dll
        self.hmap[key] = node
        self.minf = freq
        # put back handles creation in fmap
        self.put_node(node,freq)

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)