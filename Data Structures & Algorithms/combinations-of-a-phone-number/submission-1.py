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
        n = len(digits)
        res = []
        if not digits: return []
        def backtrack(i,path):
            if i == n:
                res.append("".join(path))
                return
            
            # we dont need forward metaching with already decided cahr
            # so i to n not 0 to n
            for choice in hmap[int(digits[i])]:
                # print(path)
                path.append(choice)
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res