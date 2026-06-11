class LinkedList():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        n = LinkedList(0)
        self.capacity = capacity
        self.hmap = {}
        self.lmap = {}
        self.size = 0
        self.front = n
        self.back = n

    def get(self, key: int) -> int:
        if key not in self.hmap: return -1
        
        res = self.hmap[key]

        # update it correctly to the back
        self.__remove_and_put_at_back(key)

        return res

    def __remove_and_put_at_back(self,key):
        # need to extarct the node from wherever it exists in the lmap
        # this fx also updates te back pointer correctly
        # it also updates the lmap with this node position to the new back pos
        prev = self.lmap[key]

        # special case if element being removed is teh back itself then 
        # as we need to put it in the back later we just dont do anythinga nd return ealy
        if prev.next == self.back:
            return

        # remove this entry as removed from lmap as well
        prev.next = prev.next.next
        # need to update prev.next.next prev to prev instead of the removed node
        if prev.next:
            self.lmap[prev.next.val] = prev
        self.__put_at_back(key)

    def __put_at_back(self,key):
        # put at the back in list 
        # and update back pointer as its most recent
        # it also updates the lmap
        self.lmap[key] = self.back

        self.back.next = LinkedList(key)
        self.back = self.back.next

    def put(self, key: int, value: int) -> None:
        # update path
        if key in self.hmap:
            self.hmap[key] = value
            self.__remove_and_put_at_back(key)
            return

        # new key — evict first if full
        if self.size >= self.capacity:
            key_to_remove = self.front.next.val
            self.front.next = self.front.next.next
            if self.front.next:
                self.lmap[self.front.next.val] = self.front
            self.hmap.pop(key_to_remove)
            self.lmap.pop(key_to_remove)
            self.size -= 1

        # insert at back
        self.size += 1
        self.hmap[key] = value
        if self.size == 1:
            self.lmap[key] = self.front
            self.front.next = self.back.next = LinkedList(key)
            self.back = self.back.next
        else:
            self.__put_at_back(key)



        
