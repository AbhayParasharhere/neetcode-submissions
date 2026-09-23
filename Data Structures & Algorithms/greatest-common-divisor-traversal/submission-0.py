import math
class DSU:
    def __init__(self,n):
        self.parent = [u for u in range(n)]
        self.rank = [0] * n

    def find(self,u):
        if self.parent[u] == u:
            return self.parent[u]
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb: return False

        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # basically the problem bilds down to 
        # if 2 numbers hare an gcd > 1 then they also share a shortest common prime factor 
        # > 1
        # so we can fidn all the prime factors for all teh numebrs
        # group all the vertices if they have the same prime factor
        # in the end through dsu if we have a singular ocmponent then yeah all travesal are possible
        # here insetad of doingf ro every pair , every number just groups itself onto its shortest prime factor bucket

        # we can use sieve of erasthanones witha. slight modifcation to store the sc prime factor of every number in teh sieve
        # then using that we can calcualte the shortest common prime factor of every number in nums

        # sieve works in o(nloglogrootn) around the same time complexity in the end

        MAX = int(1e5 + 5)
        sieve = [True] * MAX
        spf = list(range(MAX))

        def build_sieve():
            nonlocal sieve
            nonlocal spf
            sieve[0] = sieve[1] = False
            limit = int(math.sqrt(MAX)) + 1
            # only the left side pairs are enough
            for i in range(2,limit):
                if not sieve[i]: continue
                # fill all the multiple of i starting from i square
                for j in range(i*i,MAX,i):
                    # first time here so its spf is i
                    if sieve[j]:
                        spf[j] = i
                    sieve[j] = False
        build_sieve()

        def get_factors(x):
            prime_factors = {}
            # keep dividng the number by spf until we reach 1
            while x != 1:
                spf_now = spf[x]
                if spf_now not in prime_factors:
                    prime_factors[spf_now] = 1
                else:
                    # we are using it so increase its count
                    prime_factors[spf_now] += 1
                x = x // spf_now
            return prime_factors

        # now get the minm spf for each number and create a bucket with this
        spf_bucket = {}

        for i, num in enumerate(nums):
            factors = get_factors(num)
            
            for factor in factors.keys():
                if factor not in spf_bucket:
                    spf_bucket[factor] = []
                spf_bucket[factor].append(i)
        dsu = DSU(len(nums))
        components = len(nums)     
        # print(spf_bucket)   
        # Now union all the nodes
        for key,val in spf_bucket.items():
            till = len(val) - 1
            for i in range(till):
                j = i + 1
                if dsu.union(val[i],val[j]):
                    components -= 1
        return components == 1


