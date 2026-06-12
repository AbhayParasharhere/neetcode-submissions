class Node:
    def __init__(self,key,val,prev=None,next=None):
        self.key, self.val = key, val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # we will this time use a doubly linked list
        # every node will have its prev pointer
        # also the front and back would be dummy and be placeholders not actual elemnts
        # we maintain a linked list and a hash map sotring location of node
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.front, self.back = Node(0,0), Node(0,0)
        self.front.next = self.back
        self.back.prev = self.front

    def remove_node(self,n):
        prev = n.prev
        nxt = n.next
        n.prev.next = nxt
        nxt.prev = prev
    
    def append_back(self,n):
        # puts node n between back and back's prev node
        pre = self.back.prev
        # 4 atatchements in total
        self.back.prev = n
        n.next = self.back
        pre.next = n
        n.prev = pre

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        val = self.cache[key].val

        # to update this to the end
        self.remove_node(self.cache[key])
        self.append_back(self.cache[key])
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove_node(self.cache[key])
            self.append_back(self.cache[key])
            return
        
        if self.size >= self.capacity:
            # remove the front node next from the list and cache
            lru = self.front.next
            self.remove_node(lru)
            del self.cache[lru.key]
            self.size -= 1
        
        # put the new node at the back of the list and in cache
        node = Node(key,value)
        self.cache[key] = node
        self.append_back(node)
        self.size += 1
        
        
