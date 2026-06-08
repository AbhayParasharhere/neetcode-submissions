class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        n = len(s)
        repeat = ""
        for ch in s:
            if not ch.isdigit():
                # first append teh rpeat value into the stack as a num
                if repeat and repeat.isdigit():
                    stack.append(int(repeat))
                repeat = ""
                if ch == "]":
                    # need to process
                    str2repeat = deque()
                    while stack[-1] != "[":
                        str2repeat.appendleft(stack.pop())
                    stack.pop() # remove the "["
                    repeatCount = int(stack.pop())
                    # str2preat is reversed ude to popping order of stack
                    # but appendleft fills in rvese order to maintan correct order
                    put = "".join(str2repeat) * repeatCount
                    stack.append(put)
                else:
                    stack.append(ch)
            else:
                # for 2 or longer digit char
                repeat += ch
        res = "".join(stack)

        return res
