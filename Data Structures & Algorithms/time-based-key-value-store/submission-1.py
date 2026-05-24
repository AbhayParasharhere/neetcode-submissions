class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not isinstance(self.store.get(key), list): self.store[key] = [[timestamp,value]]
        else:
            self.store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.store.get(key): return ""
        # BS with the classic l r bounds to get closest to timestamp
        # we are looking for last F
        l = 0
        r = len(self.store[key])

        while l < r:
            m = (l+r) //2
            print(self.store[key][m][0],self.store)
            if self.store[key][m][0] > timestamp: r = m
            else: l = m + 1
        # Guard for l below 0
        if l - 1 < 0: return ""
        return self.store[key][l-1][1] 
        
