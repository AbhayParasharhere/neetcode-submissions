class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # bascially we treat teh char with its next char toegtehr if its a star
        # we can take it(the whole group) or move forward - j + 2
        # if we take it we stay her i the p group as we can take more 
        # in order to take it the char beore * must amtch the scanned char ar s 
        # so no need to track how many branches possible with a scan beforehand - we just let its can

        n = len(s)
        m = len(p)
        cache = {}
        def solve(i,j):
            # pattern exhausted and syring complet means true
            if (i,j) in cache: return cache[(i,j)]
            if j == m:
                if i == n: return True
                return False
            
            first_char_matched = False
            if i < n and (s[i] == p[j] or p[j] == "."):
                first_char_matched = True
            
            if j+1 < m and p[j+1] == "*":
                # can only take if the cur jth char matches the ith char in s or is a .
                skip_star_group = solve(i,j+2)
                take_star_group = first_char_matched and solve(i+1,j)
                # skip this star group
                if(take_star_group or skip_star_group): 
                    cache[(i,j)] = True
                    return True

            cache[(i,j)] = first_char_matched and solve(i+1,j+1)
            return cache[(i,j)]

        return solve(0,0)

