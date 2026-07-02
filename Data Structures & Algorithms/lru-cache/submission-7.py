class DLL:
    def __init__(self,key,val,next=None,prev=None):
        self.key, self.val = key, val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.hmap = {}
        self.front = DLL(0,0)
        self.back = DLL(0,0)
        self.front.next = self.back
        self.back.prev = self.front

    def put_back(self,node):
        if node.key not in self.hmap:
            self.hmap[node.key] = node
        back_prev = self.back.prev
        self.back.prev = node
        node.next = self.back

        back_prev.next = node
        node.prev = back_prev
    
    def remove_node(self,node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


    def touch(self,node):
        self.remove_node(node)
        self.put_back(node)
    def get(self, key: int) -> int:
        if not key in self.hmap: return -1

        node = self.hmap[key]
        self.touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.touch(node)
            return
        if self.size >= self.capacity:
            node2remove = self.front.next
            self.remove_node(node2remove)
            del self.hmap[node2remove.key]
            self.size -= 1
        self.size += 1
        node2put = DLL(key,value)
        self.put_back(node2put)
        
