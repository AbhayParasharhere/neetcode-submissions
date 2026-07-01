class DLL:
    def __init__(self,key,val,freq,prev=None,next=None):
        self.key, self.val, self.freq = key, val, freq
        self.next = next
        self.prev = prev

class DLLWrapper:
    def __init__(self):
        # it has a front and back pointer
        # these are dummy and are just for keeping track not for actual values
        self.front = DLL(0,0,0)
        self.back = DLL(0,0,0)
        # create link
        self.front.next = self.back
        self.back.prev = self.front
class LFUCache:

    def __init__(self, capacity: int):
        # we use a hashmap of DLL lists
        # hashmap of requency to dll lists
        self.capacity = capacity
        self.size = 0
        # hmap of frequecy to dll wrappers - useful to organzie by frequcny and keep track of min freq
        # as min freq front is alwys teh first to be removed in case we are full
        self.fmap = {}
        self.min_f = None
        # hmap of keys to node addresses - useful to remove a node and promote it
        self.hmap = {}
    
    def put_back(self,node,freq):
        if freq not in self.fmap:
            self.fmap[freq] = DLLWrapper()
        # attaches to the given freq class just before back pointer
        back = self.fmap[freq].back
        prev = back.prev

        # attach to back
        back.prev = node
        node.next = back

        # attach to prev
        node.prev = prev
        prev.next = node
    
        node.freq = freq

    def remove_node(self,node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def touch(self,node):
        freq = node.freq
        self.remove_node(node)
        self.put_back(node,freq+1)

    def update_min(self,prev_f):
        # updates the min f if its equal to prev_f
        if prev_f == self.min_f:
            # if minf class node has just single elemnt remove from fmap as well
            min_class = self.fmap[self.min_f]
            if min_class.front.next == min_class.back:
                del self.fmap[self.min_f]
                # need to update the min f as well
                self.min_f += 1

    def get(self, key: int) -> int:
        if key not in self.hmap: return -1

        node = self.hmap[key]
        prev_f = node.freq
        new_f = prev_f + 1
        # touch fx that promotes the freq class of the specified node
        self.touch(node)
        # update the min f if affected
        self.update_min(prev_f)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            # update min if affected
            self.update_min(node.freq)
            # promote the freq class
            self.touch(node)
            # update the value
            node.val = value
            return
        if self.size >= self.capacity:
            self.size -= 1
            node2remove = self.fmap[self.min_f].front.next
            self.remove_node(node2remove)
            if self.fmap[self.min_f].front.next == self.fmap[self.min_f].back:
                del self.fmap[self.min_f]
            # remove node from hmap as well
            del self.hmap[node2remove.key]
        self.size += 1
        # new ndoe always gets the min f
        self.min_f = 1
        node = DLL(key,value,self.min_f)
        self.hmap[key] = node
        self.put_back(node,self.min_f)



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)