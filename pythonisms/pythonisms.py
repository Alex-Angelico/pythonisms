# At least 3 custom generators on custom collections
# At least 5 decorators that augment function behavior
# At least 2 methods that improve code elegance

from data_classes.linked_list import LinkedList
# from data_classes.hashtable import Hashtable
from generators import gibberish_generator, hash_consistency_check
# from decorators import entry_counter
# from functools import wraps

# hashtable = Hashtable()
ll_a = LinkedList()
ll_b = LinkedList()
node_keys = gibberish_generator(20, 400)
node_values = gibberish_generator(20)

# node_keys = gibberish_generator(5, 600)
# node_values = gibberish_generator(5)
# keys = [key for key in node_keys]
# values = [value for value in node_values]
gibberish_keys = list(node_keys)
gibberish_values = list(node_values)

# for i, key in enumerate(gibberish_keys):
#     hashtable.add(key, gibberish_values[i])

for i, key in enumerate(gibberish_keys):
    ll_a.append((key, gibberish_values[i]))

for i, key in enumerate(gibberish_keys):
    ll_b.append((key, gibberish_values[i]))

# print(ll_a)
# print(ll_b)
# print(bool(ll_a == ll_b))
# print(repr(ll_a), repr(ll_b))

# for node in ll_b: print(node)

# print(keys)
print(hash_consistency_check(gibberish_keys))
# print(keys, values)
# print(hashtable.get(keys[1]))
# print(hashtable.print_hash_matches(400))
# print(hashtable.print_bucket(1008))

# print(repr(ll_a))
# print(hashtable._buckets)
# print(hashtable)
# print(106//81)

