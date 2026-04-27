class Listnode:
    def __init__(self,key,value,nxt):
        self.key = key
        self.value = value
        self.next = nxt

class MyHashMap:

    def __init__(self):
        self.arr = [Listnode(False,False,None) for _ in range(10001)]

    def put(self, key: int, value: int) -> None:
        pos = self.hash(key)
        node = self.arr[pos]
        while node.next:
            if node.next.key == key:
                # key already exist case
                # So update the value and then return
                node.next.value = value
                return
            node = node.next
        node.next = Listnode(key,value,None)

    def get(self, key: int) -> int:
        pos = self.hash(key)
        node = self.arr[pos]
        # Get through the chain to get the appropriate key
        while node.next:
            if node.next.key == key:
                return node.next.value
            node = node.next
        # Not found in the end cae
        return -1

    def remove(self, key: int) -> None:
        pos = self.hash(key)
        node = self.arr[pos]
        while node.next:
            if node.next.key == key:
                #  key exist case
                #  so skip it
                node.next = node.next.next
                return
        return
    def hash(self,key):
        return key % 10000
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)