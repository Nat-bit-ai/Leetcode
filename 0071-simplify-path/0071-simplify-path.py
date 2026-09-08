class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def pop(self):
        if self.is_empty():
            return None
        else:
            rmv_node = self.head
            self.head = self.head.next 
            rmv_node.next = None
            return rmv_node.val
    def push(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head 
            self.head = new_node
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.head.val
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = Stack()
        for i in s:
            if i == "":
                continue
            elif i == ".":
                continue
            elif i == "..":
                if not stack.is_empty():
                    stack.pop()
            else:
                stack.push(i)

        ans = []
        while not stack.is_empty():
            ans.append(stack.pop())
        ans.reverse()
        return "/" + "/".join(ans)