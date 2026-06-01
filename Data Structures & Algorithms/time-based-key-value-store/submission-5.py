class TimeMap:

    def __init__(self):
        # we are using binary search on the timestamp 
        self.obj = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 
        if key not in self.obj:
            self.obj[key] = [(value,timestamp)]
        else:
            self.obj[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        # now we have to do a binary search on the obj
         if key not in self.obj: return ""
         l = 0
         r = len(self.obj[key])

         while l < r:
            m = (l+r) // 2
            # m is a index on the keys
            # we use a first true return to return the closest
            tp = self.obj[key][m][1]
            if tp > timestamp: r = m
            else: l = m + 1
        # l points to the closest timestamp
         if l-1 >=0: 
            return str(self.obj[key][l-1][0])
         else:
            return ""
        
