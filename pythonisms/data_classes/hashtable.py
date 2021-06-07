from data_classes.linked_list import LinkedList
# from pythonisms.pythonisms.data_classes.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        # None can be replaced with LinkedList() at higher initial setup cost
        self._buckets = size * [None]

    def _hash(self, key):
        sum = 0
        for character in key: sum += ord(character)
        return (sum * 599) % self._size

    def add(self, key, value):
        hashed_key_index = self._hash(key)
        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].append((key, value))

    def get(self, key):
        requested_key = self._hash(key)
        if self._buckets[requested_key]:
            current = self._buckets[requested_key].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        else:
            return None

    def contains(self, key):
        requested_key = self._hash(key)
        if self._buckets[requested_key]:
            current = self._buckets[requested_key].head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        else:
            return False

    def __str__(self):
        populated_buckets = ''
        for index, bucket in enumerate(self._buckets):
            if bucket:
                populated_buckets += f'=========================\nBucket: {index}\n=========================\n{bucket}\n'
        populated_buckets += 'END OF LIST'
        return populated_buckets

    def print_hash_matches(self, key_sum):
        requested_key = (key_sum * 599) % self._size
        if self._buckets[requested_key]:
            return f'=========================\nBucket: {requested_key}\n=========================\n{self._buckets[requested_key]}'

    def print_bucket(self, key):
        if self._buckets[key]:
            return f'=========================\nBucket: {key}\n=========================\n{self._buckets[key]}'