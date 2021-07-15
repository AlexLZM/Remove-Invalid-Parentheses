def removeInvalidParentheses(s):
    left = right = 0
    for c in s:
        if c == '(':
            left += 1
        elif c == ')':
            if left > 0:
                left -= 1
            else:
                right += 1
    res = set()
    
    def dfs(idx, left_count, right_count, left_rem, right_rem, current):
        nonlocal res
        if idx == len(s):
            if left_count == right_count and left_rem == right_rem == 0:
                res.add(current)
        else:
            if s[idx] == '(':
                dfs(idx + 1, left_count + 1, right_count, left_rem, right_rem, current + '(')
                if left_rem > 0:
                    dfs(idx + 1, left_count, right_count, left_rem - 1, right_rem, current)
            elif s[idx] == ')':
                if left_count > right_count:
                    dfs(idx + 1, left_count, right_count + 1, left_rem, right_rem, current + ')')
                if right_rem > 0:
                    dfs(idx + 1, left_count, right_count, left_rem, right_rem - 1, current)
            else:
                dfs(idx + 1, left_count, right_count, left_rem, right_rem, current + s[idx])
    
    dfs(0, 0, 0, left, right, '')
    return res
          
