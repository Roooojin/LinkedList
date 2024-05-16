class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_in_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_at_front(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next

    def delete_at_back(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            value = current.next.value
            current.next = None
            return value

    def search(self, value):
        if self.head is None:
            return None
        else:
            q = self.head
            c = 0
            while q is not None:
                if q != value:
                    c += 1
                    q = q.next
                else:
                    return c

    def clear(self):
        self.head = None


    def size(self):
        if self.head is None:
            return None
        else:
            c=0
            q=self.head
            while q is not None:
                c+=1
                q=q.next
            return c


    def print_forward(self):
        if self.head is None:
            return None
        else:
            q=self.head
            while q is not None:
                return q.data
                q=q.next


    def print_backward(self):
        if self.head is None:
            return

        current = self.head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next

        print(' '.join(result[::-1]))

    def reverse_recursive(self):
        def reverse_util(current, prev):
            if current is None:
                self.head = prev
                return

            next_node = current.next
            current.next = prev
            reverse_util(next_node, current)

        reverse_util(self.head, None)

    def reverse_non_recursive(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

