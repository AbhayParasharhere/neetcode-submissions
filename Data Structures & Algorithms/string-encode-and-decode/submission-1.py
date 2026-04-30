class Solution:

    def encode(self, strs: List[str]) -> str:
        # Using 3$abc4$yuio scheme - len of the word + sentinel
        # Return the encoded string
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        # Returns the decoded array of words
        res, i = [], 0
        
        # Loop char and repeat until push word by word
        while i < len(s):
            # Use a second pointer j to find teh full length until u find teh sentinel
            # Purpose to get the length stored
            j = i
            word_length = 0
            while s[j] != "$":
                j += 1
            word_length = int(s[i:j])
            res.append(s[j+1:j+1+word_length])
            i = word_length + 1 + j
        return res
