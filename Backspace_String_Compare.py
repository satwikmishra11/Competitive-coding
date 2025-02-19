class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s):
            stack = []
            for char in s:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)

        return process_string(s) == process_string(t)
