class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []

        for i in s:
            if i == "":
                continue

            if i == ".":
                continue

            if i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)
