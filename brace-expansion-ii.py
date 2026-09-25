class Solution:
    def braceExpansionII(self, expression: str):

        def parse(s, i=0):
            result = set()
            parts = [set()]

            while i < len(s) and s[i] != '}':
                if s[i] == '{':
                    cur, i = parse(s, i + 1)

                elif s[i] == ',':
                    result |= parts[0]
                    parts = [set()]
                    i += 1
                    continue

                else:
                    cur = {s[i]}
                    i += 1

                parts[0] = (
                    {a + b for a in parts[0] for b in cur}
                    if parts[0]
                    else cur
                )

            result |= parts[0]

            if i < len(s) and s[i] == '}':
                i += 1

            return result, i

        return sorted(parse(expression)[0])
