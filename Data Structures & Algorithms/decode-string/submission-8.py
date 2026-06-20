class Solution:
    def decodeString(self, s: str) -> str:
        # basically like closing brack problem
        # when we encounter a ] we porcess the stack first before appedning the next cahr
        # when we are goung if we enocunter a number we store in a number string until we encounter a non number
        # then beofre pushing the non digit we first convert. the number and push it on the stack
        # this is to take care of 2 or mroe digit numbers properly

        times = ""
        stack = []

        for ch in s:
            if ch.isdigit():
                times += ch
            else:
                if times != "":
                    stack.append(int(times))
                    # reset times for future
                    times = ""
                if ch != "]":
                    stack.append(ch)
                else:
                    # we need to process stack first
                    repeat = []
                    while stack[-1] != "[":
                        repeat.append(stack.pop())
                    stack.pop() # get rid of open bracket
                    till = stack.pop()
                    # reverse as we used a stack
                    repeat = repeat[::-1]
                    res = till * "".join(repeat)
                    # print(repeat,till,stack,res)
                    stack.append(res)
        return "".join(stack)
