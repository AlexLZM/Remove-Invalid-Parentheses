# Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

## Example 1:

Input: s = "()())()"

Output: ["(())()","()()()"]
## Example 2:

Input: s = "(a)())()"

Output: ["(a())()","(a)()()"]
## Example 3:

Input: s = ")("

Output: [""]
 

## Constraints:

1 <= s.length <= 25

s consists of lowercase English letters and parentheses '(' and ')'.

There will be at most 20 parentheses in s.

## Strategy
1. Use 1 loop over s to find how many '('s and ')'s to remove.
2. build a help function that does dfs search over the string index, tracking 6 variables:
    1. index over s
    2. \# of '('s included
    3. \# of ')'s included
    4. \# of ')'s to remove
    5. \# of '('s to remove
    6. current aggregated valid string
3. if index is length of s, the search is over. Check the '('s and ')'s included, if they are equal and we have removed the needed \# of ')'s and '('s, add the current valid string to result.
4. else, if current char is '(', we have 2 choice:
    1. keep it,  so \# of '('s included + 1, current string + '('
    2. if we still have ')'s to remove, remove it, so \# of '('s to remove - 1
5. if current char is ')', we have 2 choice:
    1. if \# of '(' included is greater than ')'s included, keep it, so # of ')'s included + 1, current string + ')'
    2. if we still have '('s to remove, remove it, so \# of ')'s to remove - 1
6. if the current chat is others, current string + this char

## Time Complexity
O(2<sup>n</sup>)


