class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sort(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = merge_two_sorted_lists(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

# 1. Реверсування однозв'язного списку
print("Реверсування списку:")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()

reversed_head = reverse_linked_list(ll.head)
ll.head = reversed_head
ll.print_list()

# 2. Сортування однозв'язного списку (сортування злиттям)
print("\nСортування списку:")
unsorted_list = LinkedList()
unsorted_list.append(3)
unsorted_list.append(1)
unsorted_list.append(2)
unsorted_list.print_list()

sorted_head = merge_sort(unsorted_list.head)
unsorted_list.head = sorted_head
unsorted_list.print_list()

# 3. Об'єднання двох відсортованих однозв'язних списків
print("\nОб'єднання двох відсортованих списків:")
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list1.print_list()

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)
list2.print_list()

merged_head = merge_two_sorted_lists(list1.head, list2.head)
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.print_list()
