class DLL:
    def __init__(self,key=0,value=0,prev=None,next=None):
        self.key, self.value = key, value
        self.prev = prev
        self.next = next

class DLLWrapper:
    def __init__(self,front=None,back=None,node=None):
        self.front = DLL(0,0)
        self.back = DLL(0,0)
        self.front.next = self.back
        self.back.prev = self.front
        if node:
            node.prev = self.front
            node.next = self.back
            self.front.next = node
            self.back.prev = node
    

class LFUCache:

    def __init__(self, capacity: int):
        # we use a frq map and keep track of a dll at every freq
        # we also keep track of the lwoest freq in our fmap to remove in case of max capcity
        # why dll cos in case of get we have to update the freq of any elemnt in our stack in o1 time if we use a deque it wont be o1
        # but O n  if we use a Q to find an elemntin case of capcity ful we just pull teh front from teh lwoest freq dll
        self.hmap = {}
        self.minf = 0
        self.fmap = {}
        self.capacity = capacity
        self.size = 0

    def remove_node(self,node):
        # removes the node from its dll
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def put_node_back(self,node,freq):
        # put the node before the correct dll's self.back
        back = self.fmap[freq].back
        prev = back.prev

        # attach to the back
        node.next = back
        back.prev = node

        # attach to the prev
        prev.next = node
        node.prev = prev


    def get(self, key: int) -> int:
        if key not in self.hmap: return -1

        # we need to update the freq as it was just used
        # the hmap stroes both the freq level and the node address in the dll for this key
        pre_f, node_addr = self.hmap[key]
        # print(self.hmap[key][0])
        self.hmap[key][0] += 1

        # node is removed from thsi freq level dll
        self.remove_node(node_addr)

        # check for removal case with self.minf 
        if pre_f == self.minf:
            if self.fmap[self.minf].front.next == self.fmap[self.minf].back:
                # that means nothing is left in this dll
                del self.fmap[self.minf]
                self.minf += 1

        if pre_f + 1 not in self.fmap:
            self.fmap[pre_f + 1] = DLLWrapper()
        # put node at the new freq level dll at the back
        self.put_node_back(node_addr,pre_f+1)

        return node_addr.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.hmap:
            # update the value and the freq and ordeing within that freq
            pre_f, node_addr = self.hmap[key]
            self.hmap[key][0] += 1
            node_addr.value = value

            # node is removed from thsi freq level dll
            self.remove_node(node_addr)

            # check for removal case with self.minf 
            if pre_f == self.minf:
                if self.fmap[self.minf].front.next == self.fmap[self.minf].back:
                    # that means nothing is left in this dll
                    del self.fmap[self.minf]
                    self.minf += 1

            if pre_f + 1 not in self.fmap:
                self.fmap[pre_f + 1] = DLLWrapper()

            # put node at the new freq level dll at the back
            self.put_node_back(node_addr,pre_f+1)
            return
        
        if self.size >= self.capacity:
            # we need to remove the lowest freq dll front
            to_remove = self.fmap[self.minf].front.next
            self.remove_node(to_remove)
            del self.hmap[to_remove.key]
            self.size -= 1
        # we need to create a new freq level of 1 for this node 
        self.size += 1
        freq = 1
        self.minf = 1
        node = DLL(key,value)
        self.hmap[key] = [freq,node]
        if freq not in self.fmap: 
            self.fmap[freq] = DLLWrapper(node=node)
        else:
            self.put_node_back(node,freq)




            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)