class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        st = ['']

        for i in s:
            if i == '(':
                st.append('')
            elif i == ')':
                reversed_chars = st.pop()[::-1]
                st[-1] += reversed_chars
            else:
                st[-1] += i
        return st.pop()
