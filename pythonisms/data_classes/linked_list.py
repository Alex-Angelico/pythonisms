from functools import wraps

def entry_counter(function):
    @wraps(function)
    def added_info(*args, **kwargs):
        base = function(*args, **kwargs)
        number = base.count('\n')
        return f'{base}\n=========================\n{number} line entries\n=========================\n'
    return added_info

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value=None):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current != None:
            if current.getValue() == value:
                return True
            else:
                current = current.getNext()
        return False

    def append(self, value):
        node = Node(value)
        current = self.head
        if current == None:
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node

    def insertBefore(self, value, newVal):
        node = Node(newVal)
        current = self.head
        if current == None:
            self.head = node
        elif current.value is value:
            self.insert(newVal)
        else:
            while current != None:
                if current.next.value == value:
                    node.next = current.next
                    current.next = node
                    break
                else:
                    current = current.next

    def insertAfter(self, value, newVal):
        current = self.head
        while current:
            if current.value == value:
                node = Node(newVal, current.next)
                current.next = node
                return
            current = current.next
        return "Target value not in list."

    def delete(self, value):
        current = self.head
        if current == None:
            print("No nodes in list.")
        elif current.value is value:
            self.head = current.next
        else:
            while current.next.value != value:
                current = current.next
            current.next = current.next.next

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()

    def __len__(self):
        return len(list(iter(self)))

    def __getitem__(self, index):
        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError

    @entry_counter
    def __str__(self):
        bucket = ''
        for value in self:
            bucket += f'Key:{value[0]} | Value:{value[1]}\n'
        bucket += 'None'
        return bucket

    def __repr__(self):
        return str(self.head)

    def __eq__(self, other):
        return list(self) == list(other)


    def kthFromEnd(self, k):
        # node_list = []
        # current = self.head

        # while current != None:
        #     node_list.append(current.value)
        #     current = current.next
        # if abs(k) > len(node_list):
        #     return 'Index value greater than list length.'
        # if k < 0:
        #     return node_list[abs(k)]
        # else:
        #     return node_list[len(node_list) - k - 1]
        head_start = 0
        follower = None
        leader = self.head
        while leader:
            leader = leader.next
            if follower:
                follower = follower.next
            elif head_start == k:
                follower = self.head
            else:
                head_start += 1
        if not follower:
            return "Target index value greater than list length."
        return follower.value

    # def __str__(self):
    #     current = self.head
    #     node_list = []
    #     node_output = ""
    #     while current != None:
    #         node_list.append(f"{ {current.value} } -> ")
    #         current = current.next
    #     node_list.append("NULL")
    #     for node in node_list:
    #         node_output += node
    #     return node_output
