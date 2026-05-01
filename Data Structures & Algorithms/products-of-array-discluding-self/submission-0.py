class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Need to use prefix multiple arrays here - question is how
        # 1 2 4 6
        # Output = 2*4*6 1*4*6 1*2*6 1*2*4 = 48 24 12 8
        # 1 2 4 6 
        # okay so the idea is at every position put the prefix array multiple to the left * postfix to the right
        # this gives the result for that positon
        n = len(nums)
        postfix = [1 for _ in range(n)]
        prefix = [1 for _ in range(n)]
        res = [1 for _ in range(n)]

        for i in range(n):
            if i >=1:
                prefix[i] = prefix[i-1] * nums[i]
            else:
                prefix[i] = nums[i]
        
        for i in range(n-1,-1,-1):
            if i < n-1:
                postfix[i] = postfix[i+1] * nums[i]
            else:
                postfix[i] = nums[i]

        for i in range(n):
            pre = 1
            post = 1
            if i - 1 >= 0:
                pre = prefix[i-1]
            if i + 1 < n:
                post = postfix[i+1]
            res[i] = pre * post 
            
        return res


