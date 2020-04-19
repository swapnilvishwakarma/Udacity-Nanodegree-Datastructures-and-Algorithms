class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_head = self.head
        output_string = ""
        while current_head:
            output_string += str(current_head.value) + " -> "
            current_head = current_head.next
        return output_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    combined_llist = set()

    position = llist_1.head
    while position:
        combined_llist.add(position.value)
        position = position.next

    position = llist_2.head
    while position:
        combined_llist.add(position.value)
        position = position.next

    union_list = LinkedList()
    for i in combined_llist:
        union_list.append(i)

    return union_list


def intersection(llist_1, llist_2):
    llist_1_set = set()
    llist_2_set = set()

    position = llist_1.head
    while position:
        llist_1_set.add(position.value)
        position = position.next

    position = llist_2.head
    while position:
        llist_2_set.add(position.value)
        position = position.next

    intersection_set = [i for i in llist_1_set if i in llist_2_set]

    intersection_list = LinkedList()
    for i in intersection_set:
        intersection_list.append(i)

    return intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('\nUnion of LinkedLists 1 and 2:')
# Union of LinkedLists 1 and 2:

print(union(linked_list_1, linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->

print('Intersection of LinkedLists 1 and 2:')
# Intersection of LinkedLists 1 and 2:

print(intersection(linked_list_1, linked_list_2))
# 4 -> 6 -> 21 ->


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1, 35]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('\nUnion of LinkedLists 3 and 4:')
# Union of LinkedLists 3 and 4:

print(union(linked_list_3, linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->

print('Intersection of LinkedLists 3 and 4:')
# Intersection of LinkedLists 3 and 4:

print(intersection(linked_list_3, linked_list_4))
# 35 ->


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3, 2, 4, 8, 42, 33, 1, 2]
element_2 = [1, 3, 5, 7, 4, 5]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print('\nUnion of LinkedLists 5 and 6:')
# Union of LinkedLists 5 and 6:

print(union(linked_list_5, linked_list_6))
# 33 -> 2 -> 3 -> 4 -> 1 -> 5 -> 7 -> 8 -> 42 ->

print('Intersection of LinkedLists 5 and 6:')
# Intersection of LinkedLists 5 and 6:

print(intersection(linked_list_5, linked_list_6))
# 3 -> 4 -> 1 ->
