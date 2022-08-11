#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    # everything that is opened has to be closed before another thing can be opened
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{': # opening bracket
                stack.append(c)
            else: # closing bracket
                if len(stack) == 0:
                    # that means we don't any opening bracket
                    return False
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        # if we ended up with more than 0 elements in the stack,
        # then we have an unclosed brackets
        return len(stack) == 0
# @lc code=end

# ----------------------My failed attempt----------------------

#         def checkSquare(para):
#             if '[' in para:
#                 if ']' in para:
#                     squareIndex = para.index('[')
#                     for square in range(squareIndex, len(para)):
#                         if para[square] == ']':
#                             para.pop(square)
#                             para.pop(squareIndex)
#                             return checkSquare(para)
#                         else:
#                             return False
#                 # if it went through the whole list and didn't find a ')'
#                 # in other words, if it went throught the whole for loop
#                 # with the if statement never being executed
#                 # the else statement will be executed
#                 else:
#                     return False
#             elif ']' in para:
#                 return False
#             return True

#         def checkCurly(para):
#             if '{' in para:
#                 if '}' in para:
#                     curlyIndex = para.index('{')
#                     for curly in range(curlyIndex, len(para)):
#                         if para[curly] == '}':
#                             para.pop(curly)
#                             para.pop(curlyIndex)
#                             return checkCurly(para)
#                 else:
#                     return False
#             elif '}' in para:
#                 return False
#             return True

#         def checkParen(para):
#             if '(' in para:
#                 if ')' in para:
#                     parenIndex = para.index('(')
#                     for paren in range(parenIndex, len(para)):
#                         if para[paren] == ')':
#                             para.pop(paren)
#                             para.pop(parenIndex)
#                             return checkParen(para)
#                 else:
#                     return False
#             elif ')' in para:
#                 return False
#             return True
#         para = list(s)
#         while para != []:
#             if '(' in para:
#                 if ')' in para:
#                     smoothIndex = para.index('(')
#                     closingSmooth = para.index(')')
#                     paraTest = para[smoothIndex+1:closingSmooth]
#                     if checkSquare(paraTest) and checkCurly(paraTest):
#                         for smooth in range(smoothIndex, len(para)):
#                             if para[smooth] == ')':
#                                 para.pop(smooth)
#                                 para.pop(smoothIndex)
#                                 break
#                 else:
#                     return False

#             if '{' in para:
#                 if '}' in para:
#                     curlyIndex = para.index('{')
#                     closingCurly = para.index('}')
#                     paraTest = para[curlyIndex:closingCurly]
#                     if checkParen(paraTest) and checkSquare(paraTest):
#                         for curly in range(curlyIndex, len(para)):
#                             if para[curly] == '}':
#                                 para.pop(curly)
#                                 para.pop(curlyIndex)
#                                 break
#                 else:
#                     return False
#             elif '}' in para:
#                 return False
#             if '[' in para:
#                 if ']' in para:
#                     squareIndex = para.index('[')
#                     closingSquare = para.index(']')
#                     paraTest = para[squareIndex:closingSquare]
#                     if checkCurly(paraTest) and checkParen(paraTest):
#                         for square in range(squareIndex, len(para)):
#                             if para[square] == ']':
#                                 para.pop(square)
#                                 para.pop(squareIndex)
#                                 break
#                 else:
#                     return False
#             elif ']' in para:
#                 return False
#         return True
