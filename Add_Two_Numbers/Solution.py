"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

非负整数用链表表示，链表位数倒序，即表头存放最低位
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1 = ListNode(l1[0])
        ll2 = listNode(l2[0])
        
        while i < len(l1) :  
            k = ll1.next
            while k != None:
                #k = ll1.

                    
                 
            ll1.next = ListNode(l1[i])
            i += 1

        while i < len(l2) :       
            ll2.next = ListNode(l2[i])
            i += 1
            
        ret = ListNode(0)
        cl1 = l1
        cl2 = l2

        while cl1 != None or cl2 != None:
            sumVal = cl1.val + cl2.val
            if sumVal >= 10:
                ret.val = sumVal % 10
                if l1.next == None:
                    l1.next = ListNode(1)
                else:
                    l1.next.val += 1
            else:
                ret.val = sumVal
            cl1 = l1.next
            cl2 = l2.next
        return ret

so = Solution()
so.addTwoNumbers([2,4,3],[5,6,4])


            
