class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = deque()

        timesStr = ""
        r = 0
        while r < n:
            ch = s[r]
            if ch.isdigit():
                timesStr += ch
            else:
                if timesStr != "": 
                    stack.append(timesStr)
                    timesStr = ""
                if ch != "]":
                    # first append the timesStr if not a ""
                    # we are at first non digit point
                    stack.append(ch)
                else:
                    # we must process until we find the opening bracket
                    toRepeat = []
                    while stack and stack[-1] != "[":
                        toRepeat.append(stack.pop())
                    toRepeat.reverse()
                    if stack: stack.pop() #get rid of "["
                    # get the timeStr
                    times = 1
                    if stack: times = int(stack.pop())
                    toAppend = "".join(toRepeat) * int(times)
                    stack.append(toAppend)
                    timesStr = ""
            r += 1

        return "".join(list(stack))
