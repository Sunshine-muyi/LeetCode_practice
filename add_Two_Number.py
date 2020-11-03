# 给出两个非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import NewType


class ListNode:
    def __init__(self, val=0, next_Node=None):
        self.val = val
        self.next_Node = next_Node


ListNode = NewType('ListNode')


class Solution:
    def add_Two_Numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1
        else:
            pass




if __name__ == '__main__':
    pass
