"""
File: add2.py
Name: Chien-Wei Peng
------------------------
TODO:create a linked list to present a sum of two numbers.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer

    @staticmethod
    # this is a method to add a new list node at the end of a linked list.
    def append_node(list_node, new_node):
        cur = list_node
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    number1 = number_calculator(l1)
    number2 = number_calculator(l2)
    ans = number1 + number2
    l3 = make_linked_list(ans)
    return l3


def number_calculator(linked_list: ListNode) -> int:
    """
    The function will get the number of linked list
    """
    cur = linked_list
    count = 0
    number = 0
    while cur is not None:
        count += 1
        number += cur.val * (10 ** (count - 1))
        cur = cur.next
    return number


def make_linked_list(ans: int) -> ListNode:
    """
    The function will get linked list from a number.
    """
    l3 = None
    while True:
        new_node = ListNode((ans % 10), None)
        ans = ans // 10
        # add first Node
        if l3 is None:
            l3 = new_node
        else:
            # add new node
            l3.append_node(l3, new_node)
        if ans == 0:
            return l3


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
