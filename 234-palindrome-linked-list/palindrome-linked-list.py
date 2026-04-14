class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        r = 0 
        l = len(arr) - 1
        while r < l:
            if arr[l] != arr[r]:
                return False
            l -= 1
            r += 1
        return True