class DLL:
    def __init__(self,key,val,next=None,prev=None):
        self.key,self.val = key,val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # use a dll to isnert and remove quickly from the dummy front and back
        # when anything is get our put that is tehre we touch it and move it just before back
        # we remove from the front
        self.front = DLL(0,0)
        self.back = DLL(0,0)
        self.size = 0
        self.capacity = capacity
        # maps key to node in DLL
        self.hmap = {}
        # forma. dll
        self.front.next = self.back
        self.back.prev = self.front

    def put_back(self,node):
        # Remove from its current pos and put at the most recent used back before dummy back
        prev = self.back.prev

        # attach to prev
        prev.next = node
        node.prev = prev

        # attach to back
        node.next = self.back
        self.back.prev = node
    
    def remove_node(self,node):
        # removes from its current pos in dll
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    
    def touch(self,node):
        # remove from its cur position
        # then put at the back where most recently used are present
        self.remove_node(node)
        self.put_back(node)


    def get(self, key: int) -> int:
        if key not in self.hmap: return -1

        node = self.hmap[key]
        # touch to remove from its current pos and put at the most recent used back
        self.touch(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            # update the value as well
            node.val = value
            self.touch(node)
            return
        if self.size >= self.capacity:
            # remove teh lest fre node at after teh front of DLL
            node2remove = self.front.next
            self.remove_node(node2remove)
            del self.hmap[node2remove.key]
            self.size -= 1
        node = DLL(key,value)
        # put in hmap
        self.hmap[key] = node
        self.put_back(node)
        self.size += 1
        
