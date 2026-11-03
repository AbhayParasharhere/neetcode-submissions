class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }
        if not digits: return []
        n = len(digits)
        res = []
        # a simple combinations question 
        res = []
        def solve(at,path):
            # print(path)
            if len(path) == n:
                res.append("".join(path))
                return
            
            # each letter has k choices as per their hashmap
            # we choose all of them for making our path
            # there is no skip branch as its not allowed we take for sure
            choices = hmap[int(digits[at])]
            for choice in choices:
                path.append(choice)
                solve(at+1,path)
                # undo for futrue brances
                path.pop()
        solve(0,[])
        return res
            
                
