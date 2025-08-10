class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for b in s:
            if b in brackets_map: stack.append(b)
            elif not stack or brackets_map[stack.pop()] != b: return False
        return not stack
