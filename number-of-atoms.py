class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            stack = [Counter()]
            i, n = 0, len(formula)
            
            while i < n:
                if formula[i] == '(':
                    stack.append(Counter())
                    i += 1
                elif formula[i] == ')':
                    top = stack.pop()
                    i += 1
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[i_start:i] or 1)
                    for elem, count in top.items():
                        stack[-1][elem] += count * multiplicity
                else:
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    elem = formula[i_start:i]
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[i_start:i] or 1)
                    stack[-1][elem] += multiplicity
            
            return stack.pop()
        
        count = parse()
        return ''.join(f"{elem}{(count[elem] if count[elem] > 1 else '')}" for elem in sorted(count))
