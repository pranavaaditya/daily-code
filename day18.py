
#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#Example 2:

#Input: list1 = [], list2 = []
#Output: []
#Example 3:

#Input: list1 = [], list2 = [0]
#Output: [0]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Dummy node to simplify list handling
        current = dummy  # Pointer to build the merged list

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining part of the non-empty list
        current.next = list1 if list1 else list2

        return dummy.next  # Return the merged list, skipping the dummy node

# Helper function to convert a list to a linked list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Example Usage
list1 = create_linked_list([1,2,4])
list2 = create_linked_list([1,3,4])

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)
print_linked_list(merged_head)  # Output: [1,1,2,3,4,4]
