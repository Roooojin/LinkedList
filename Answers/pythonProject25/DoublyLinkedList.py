class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_backward(self):
        if self.head is None:
            return

        current = self.tail
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.prev

        print(' '.join(result))

    def reverse_recursive(self):
        def reverse_util(current):
            if current is None:
                return

            next_node = current.next
            current.next = current.prev
            current.prev = next_node

            if current.prev is None:
                self.tail = current

            reverse_util(next_node)

        reverse_util(self.head)
        self.head, self.tail = self.tail, self.head

    def reverse_non_recursive(self):
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node

            if current.prev is None:
                self.tail = current

            current = next_node

        self.head, self.tail = self.tail, self.head

    def make_doubly(self, singly_linked_list):
        current = singly_linked_list.head
        while current is not None:
            new_node = Node(current.data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

            current = current.next

    def shift(self, num):
        if num == 0:
            return

        if num > 0:
            for _ in range(num):
                self.tail.next = self.head
                self.head.prev = self.tail
                self.head = self.head.next
                self.head.prev = None
                self.tail = self.tail.next
                self.tail.next = None
        else:
            for _ in range(abs(num)):
                self.head.prev = self.tail
                self.tail.next = self.head
                self.tail = self.tail.prev
                self.tail.next = None
                self.head.prev = None
                self.head = self.tail

    def get_size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at_position(self, data, position):
        if position < 0 or position > self.get_size():
            raise IndexError("Invalid position")

        if position == 0:
            self.insert_at_beginning(data)
        elif position == self.get_size():
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            current = self.head
            count = 0
            while count < position - 1:
                current = current.next
                count += 1

            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            raise IndexError("The list is empty")

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.is_empty():
            raise IndexError("The list is empty")

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_at_position(self, position):
        if self.is_empty():
            raise IndexError("The list is empty")

        if position < 0 or position >= self.get_size():
            raise IndexError("Invalid position")

        if position == 0:
            self.delete_at_beginning()
        elif position == self.get_size() - 1:
            self.delete_at_end()
        else:
            current = self.head
            count = 0
            while count < position:
                current = current.next
                count += 1

            current.prev.next = current.next
            current.next.prev = current.prev

    def print_forward(self):
        if self.is_empty():
            return

        current = self.head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next

        print(' '.join(result))
