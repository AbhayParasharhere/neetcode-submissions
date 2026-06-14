class DLL:
    def __init__(self,freq,key=0,val=0,prev=None,next=None):
        self.key, self.val, self.freq = key,val,freq
        self.prev = prev
        self.next = next

class DLLWrapper:
    def __init__(self):
        self.front = DLL(0,0)
        self.back = DLL(0,0)
        # make it dll
        self.front.next = self.back
        self.back.prev = self.front


class LFUCache:

    def __init__(self, capacity: int):
        # we use a minf tracker to keep track of lowest freq
        # we use a hmap mapping frequency to dll 
        # why dll as when get or put update works - we will need to remove a node in o1 time from a freq level
        # to put in the above freq level, dll supports this well
        # we have a fmap of key -> dllWrapper which just has a DLL its own front and back
        # each node in the DLL will have their key,val,freq, and prev, next 

        # when a new node comes for the frist times, teh freq 1 becoems the lwoest freq
        # when all nodes in the lowest freq dll are deleted we updaet lwoest to l + 1

        self.capacity = capacity
        self.size = 0
        self.fmap = {}
        self.minf = None
        # hmap maps keys to node_addr
        self.hmap = {}

    def remove_node(self,node):
        # removes a node from a dll
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def update_min(self):
        front = self.fmap[self.minf].front
        back = self.fmap[self.minf].back
        if front.next == back and back.prev == front:
            # no node left so delte this key from fmap
            del self.fmap[self.minf]
            self.minf += 1
    
    def put_node(self,node,freq):
        # we put it before the back of the given freq dll
        if freq not in self.fmap:
            self.fmap[freq] = DLLWrapper()
        back = self.fmap[freq].back
        prev = back.prev

        # attach to back
        node.next = back
        back.prev = node

        # attach to prev
        node.prev = prev
        prev.next = node
        

    def get(self, key: int) -> int:
        if key not in self.hmap: return -1

        node = self.hmap[key]
        pre_f = node.freq
        new_f = pre_f + 1
        node.freq = new_f

        # we need to move this node to the correct dll
        # by removing it first and then putitng in the new_f dll
        self.remove_node(node)

        # if it was the last node in the lowest freq array - we need to update 
        # the min_f and 
        if self.minf and pre_f == self.minf:
            self.update_min()
        
        self.put_node(node,new_f)

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0: return

        if key in self.hmap:
            # we update the value
            node = self.hmap[key]
            node.val = value

            # update the freq
            pre_f = node.freq
            new_f = pre_f + 1
            node.freq = new_f

            #remove the node from its dll to a higher freq dll
            self.remove_node(node)

            # update minf if necessary
            if self.minf and pre_f == self.minf:
                self.update_min()
            
            self.put_node(node,new_f)
            return
        
        if self.size >= self.capacity:
            # remove the node from the front of the lowest freq dll
            node2remove = self.fmap[self.minf].front.next
            self.size -= 1
            self.remove_node(node2remove)
            # in this case only we have to remove it from the hmap as well
            del self.hmap[node2remove.key]
            # check if it caused the need to min to change
            self.update_min()
        
        # new node so min is always 1 for now
        self.minf = 1
        self.size += 1
        node = DLL(1,key,value)
        # ensure to put the addr in the hmap
        self.hmap[key] = node

        # put the node in the correct fmap dll
        self.put_node(node,1)




        



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)