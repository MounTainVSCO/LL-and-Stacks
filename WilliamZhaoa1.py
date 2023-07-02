##
# Student Name: William Zhao
# Course: CIS 501 Data Structures and Algorithms
# Application: Linked Lists and Stacks 
# Description: Test Driver for Linked Lists and Stacks 
# Version: Python 3.11
# Solution File: WilliamZhaoa1.py
# Date: 07/6/23
# Time Complexity O(N) - time it takes to run the code 
#                        increases linearly with the size of 
#                        the input (length of string).
# Memory O(N), O(1) - Memory increases with the amount of 
#                     opening parentheses
##

from WilliamZhaostack import Stack

open_paren = ['(', '[', '{']
closed_paren = [')', ']','}']
valid_symbols = ['(', '[', '{',')', ']', '}']

def isBalanced(parenString):

    
    stack = Stack()
    stack.create_stack()
    curr_idx = 0
    while curr_idx < len(parenString):
        if parenString[curr_idx] == ' ':
            curr_idx += 1
            continue
        elif parenString[curr_idx] not in valid_symbols:
            return False
        else:
            if (parenString[curr_idx] in open_paren):
                stack.push(parenString[curr_idx])
            else:
                closing=closed_paren.index(parenString[curr_idx])
                if (stack.is_empty() or open_paren[closing]!=stack.peek()):
                    return False
                else:
                    stack.pop()
        curr_idx += 1

    return stack.is_empty()
    
def main():
    print('Check if parenthesis are balanced (type esc to exit): ')
    inp = str(input('Enter a string of parenthesis: '))
    while inp != 'esc':
        print(isBalanced(inp))
        inp = str(input('Enter a string of parenthesis: '))
 

if __name__ == '__main__':
    main()

# Test Run Validation

""" 
Check if parenthesis are balanced (type esc to exit):

Enter a string of parenthesis: ([|)]
False
Enter a string of parenthesis: () (() [()])
True
Enter a string of parenthesis: {{([][])}()}
True

Enter a string of parenthesis: hello world 
False
Enter a string of parenthesis: ()))))))
False
Enter a string of parenthesis: (]
False 
"""


