class DLL:
    def __init__(self,key,val,freq,prev=None,next=None):
        self.key, self.val, self.freq = key, val, freq
        self.prev = prev
        self.next = next

class DLLWrapper:
    def __init__(self):
        self.back = DLL(0,0,0)
        self.front = DLL(0,0,0)

        # create link
        self.front.next = self.back
        self.back.prev = self.front

class LFUCache:

    def __init__(self, capacity: int):
        # we maintain a hmap to node address
        # why - because we need to lookup if exists and quickly get to it that specific dll and remove it
        # from its current DLL frequency and update it to a higher freq DLL if need be
        # we maintian a frequency map to Double Linked List wrapper - each wrapper has front and back
        # this gives us ability toa access each frequecy DLL front and back dummy pointer 
        # this is needed as we need to remove stuff from the lowest freq DLL front in case capcity reached
        # we maintain a cur lowest freq variable at all times as we need to pop its front next quickly
        self.hmap = {}

        # each node stores its freq,key,val,next,prev 
        self.fmap = {}
        self.capacity = capacity
        self.size = 0
        self.minf = None
    
    def update_min(self,pre_f):
        # Responsible for updating 
        # minf if it is empty
        if pre_f == self.minf:
            # check if its empty
            if self.fmap[self.minf].front.next == self.fmap[self.minf].back:
                del self.fmap[self.minf]
                self.minf += 1

    def remove_node(self,node):
        # removes a node from its dll
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def put_back(self,node,new_f):
        # puts into a new f list 
        if new_f not in self.fmap:
            self.fmap[new_f] = DLLWrapper()
        
        back = self.fmap[new_f].back
        prev_back = back.prev

        # attach to back
        back.prev = node
        node.next = back

        # attach to prev
        prev_back.next = node
        node.prev = prev_back
        
    def touch(self, node):
        # handles everythingf rom removing to addings to new f dll

        # we need to increase its ferq and updaete teh node to teh correct dll
        pre_f = node.freq
        new_f = pre_f + 1
        node.freq = new_f

        self.remove_node(node)
        self.update_min(pre_f)

        self.put_back(node,new_f)

    def get(self, key: int) -> int:
        if key not in self.hmap: return -1
        node = self.hmap[key]
        self.touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.hmap:
            node = self.hmap[key]
            self.touch(node)
            # update the value
            node.val = value
            return
        if self.size >= self.capacity:
            # remove from the front
            node2remove = self.fmap[self.minf].front.next
            self.remove_node(node2remove)
            self.update_min(self.minf)
            del self.hmap[node2remove.key]
            self.size -= 1
        self.size += 1
        node2insert = DLL(key,value,1)
        self.hmap[key] = node2insert
        # definietly now 1 is the new min
        self.minf = 1
        self.put_back(node2insert,1)


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)