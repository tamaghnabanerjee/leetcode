'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''
def generate_parenthesis(n):
    stack=[]
    result=[]
    def generate(open_count,closed_count):
        if open_count==closed_count==n:
            result.append("".join(stack))
            return
        if open_count<n:
            stack.append("(")
            generate(open_count+1,closed_count)
            stack.pop()
        if closed_count<open_count:
            stack.append(")")
            generate(open_count,closed_count+1)
            stack.pop()
    generate(0,0)
    return result

if __name__=='__main__':
    n=3
    print(generate_parenthesis(n))