class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node does not exist.')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return

        prev_node.next = curr_node.next
        curr_node = None
        return

    def delete_node_at_pos(self, pos):
        if self.head:
            curr_node = self.head
            if pos == 0:
                self.head = curr_node.next
                curr_node = None
                return

            prev_node = None
            count = 0
            while curr_node and count != pos:
                prev_node = curr_node
                curr_node = curr_node.next
                count += 1

            if curr_node is None:
                return

            prev_node.next = curr_node.next
            curr_node = None

    def len_iterative(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_node_1 = None
        curr_node_1 = self.head
        while curr_node_1 and curr_node_1.data != key_1:
            prev_node_1 = curr_node_1
            curr_node_1 = curr_node_1.next

        prev_node_2 = None
        curr_node_2 = self.head
        while curr_node_2 and curr_node_2.data != key_2:
            prev_node_2 = curr_node_2
            curr_node_2 = curr_node_2.next

        if not curr_node_1 or not curr_node_2:
            return

        if prev_node_1:
            prev_node_1.next = curr_node_2
        else:
            self.head = curr_node_2

        if prev_node_2:
            prev_node_2.next = curr_node_1
        else:
            self.head = curr_node_1

        curr_node_1.next, curr_node_2.next = curr_node_2.next, curr_node_1.next

    def reverse_iterative(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nxt
        self.head = prev_node

    def reverse_recursive(self):
        def __reverse_recursive(curr_node, prev_node):
            if not curr_node:
                return prev_node

            nxt = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nxt
            return __reverse_recursive(curr_node, prev_node)

        self.head = __reverse_recursive(self.head, None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q

        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        curr_node = self.head
        prev_node = None
        duplicates = dict()
        while curr_node:
            if curr_node.data in duplicates:
                prev_node.next = curr_node.next
                curr_node = None
            else:
                duplicates[curr_node.data] = 1
                prev_node = curr_node
            curr_node = prev_node.next
