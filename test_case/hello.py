# -*- coding:utf-8 -*-
# fibonacci数


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 法1 哈希表
        if head == None or head.next == None:
            return False
        node_set = set()
        while head:
            if head in node_set:
                return True
            else:
                node_set.add(head)
            head = head.next
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针法
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


