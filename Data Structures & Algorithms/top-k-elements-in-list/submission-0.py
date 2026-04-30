class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Logic - Create count map
        # by value of map - push to bucket sort array 
        # extract from end of bucket till k for the final outpute

        cMap = {}
        bucket = [[] for _ in range(len(nums))]
        res = []
        for num in nums:
            if num not in cMap:
                cMap[num] = 1
            else:
                cMap[num] += 1

        # print(cMap,bucket,res)
        for key, val in cMap.items():
            # Push to appropriate index in the bucket
            bucket[val - 1].append(key)
        
        # build final result
        for i in range(len(bucket) - 1,-1,-1):
            if len(bucket[i]) >=1:
                for item in bucket[i]:
                    if len(res) < k:
                        res.append(item)
                    else:
                        break
        return res