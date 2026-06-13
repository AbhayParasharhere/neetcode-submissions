class DLL:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key, self.val = key, val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # we use a hmap for key to linked list node pair 
        # why - so that we are able to stich any node from within
        # we are using a doubly linked list as this stiching will rely on prev node
        # and dll preseves this info nicely
        # we also store the key, value , prev, next in the node itself
        # so essentially we are mainitaing a hmap and another dll list
        # why hasmap for checking in o1 and dll fro stiching recently used to the back of the list
        # we use 2 sentinel dummy nodes which never point to real value but act as gates for front and back
        self.hmap = {}
        self.front = DLL(0,0)
        self.back = DLL(0,0)
        self.capacity = capacity
        self.size = 0

        # form a link bw them
        self.front.next = self.back
        self.back.prev = self.front

    def remove_node(self,node):
        prev = node.prev
        nxt = node.next

        # this removes the node between them
        node.prev.next = nxt
        nxt.prev = prev
    
    def put_back(self,node):
        # we put it just before back pointer
        prev = self.back.prev

        # attach node to prev
        prev.next = node
        node.prev = prev
        # attach node to back
        node.next = self.back
        self.back.prev = node

    def get(self, key: int) -> int:
        if key not in self.hmap: return -1

        node = self.hmap[key]

        # update as its most recent used by updating to back of dll
        self.remove_node(node)
        self.put_back(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            # update to the end of the dll this node
            self.remove_node(node)
            self.put_back(node)
            return
        
        if self.size >= self.capacity:
            # we need to remove the node after the front pointer for space
            after_front_node = self.front.next
            del self.hmap[after_front_node.key]
            self.remove_node(after_front_node)
            self.size -= 1
        
        # put the new node in the back and the hmap
        self.size += 1
        put_node = DLL(key,value)
        self.hmap[key] = put_node
        self.put_back(put_node)
        
