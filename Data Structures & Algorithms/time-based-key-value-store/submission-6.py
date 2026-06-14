class TimeMap:

    def __init__(self):
        # we have a hmap where key maps to an array of (val,timestamp) tuple
        # we can lok into this array through bs with timestamp as set is called naturally with higher and higher timestamp
        # this creates a sorte dformat of timestamp for us to use bs
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = [(value,timestamp)]
        
        self.hmap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap: return ""

        arr = self.hmap[key]
        n = len(arr)
        l = 0
        r = n

        # montonicity such that we find first timestamp greater than it - then return last false
        # this ast false will be laregst which is <= to the given timestamp
        while l < r:
            m = (l+r) // 2
            if arr[m][1] > timestamp: r = m
            else: l = m + 1
        if l - 1 < 0: return ""

        return arr[l-1][0]

        
