
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s): 
        """
        Checks if a string of brackets is valid.
        Args:
            s: The string containing brackets.
        Returns:
            True if the string is valid, False otherwise.
        """
        stack = []
        matching_brackets = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in matching_brackets:
                top_element = stack.pop() if stack else '#'
                if matching_brackets[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
print(sol.isValid(""))
print(sol.isValid("((()))"))
print(sol.isValid("{{{{"))
print(sol.isValid("}}}}"))