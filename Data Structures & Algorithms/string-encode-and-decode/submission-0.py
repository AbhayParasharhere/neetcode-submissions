class Solution:

    def encode(self, strs: List[str]) -> str:
        # Takes an array of string and return an encoded string
        # Best scheem is to have len of character encoded after symbol so u knwo where the next symbol is
        # symbol after length, $5 means after 5 char 
        # $num$ num points to the next word $ start
        # $0$ for the empty string
        res = ""
        for st in strs:
            res += "$"
            res += str(len(st))
            res += "$"
            res += st
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        # Look for the first $
        i = 0
        length = ""
        while i < len(s):
            if s[i] == "$":
                i += 1 # Advance to the number start of length
                # input the length data until u find the $ to end the length
                while s[i] != "$":
                    length += s[i]
                    i += 1
                i += 1 # advance pointer from $ to start of word
            print("len",length)
            word_count = 0
            word = ""
            till = 0
            if length != "":
                till = int(length)
            while word_count < till:
                word += s[i]
                word_count += 1
                i += 1
            res.append(word)
            length = ""
            till = 0

        return res
