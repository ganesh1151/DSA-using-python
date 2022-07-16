def isMatching(a,b):
    if (a=="(" and b==")") or (a=="{" and b=="}") or \
            (a=="[" and b=="]"):
        return True
    else:
        return False


def isBalanced(exoer):
    stack=[]
    for x in exoer:
        if x in ("(","{","["):
            stack.append(x)
        else:
            if not stack:
                return False
            elif isMatching(stack[-1],x)==False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

a=input()

print(isBalanced(a))

a=input()

print(isBalanced(a))



#OUTPUT
"""
{{[]{{(())}}}}
True
[[[[[{{))}}}}}
False
"""