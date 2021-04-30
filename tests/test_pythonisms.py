import pytest
from pythonisms.pythonisms.decorators import entry_counter
from pythonisms.pythonisms.generators import gibberish_generator, hash_consistency_check
from pythonisms.pythonisms.data_classes.linked_list import LinkedList
from pythonisms.pythonisms.data_classes.hashtable import Hashtable

@pytest.fixture(scope='session')
def test_structures():
    hashtable = Hashtable()
    ll_a = LinkedList()
    ll_b = LinkedList()

    node_keys = gibberish_generator(20, 400)
    node_values = gibberish_generator(20)
    gibberish_keys = list(node_keys)
    gibberish_values = list(node_values)

    for i, key in enumerate(gibberish_keys):
        hashtable.add(key, gibberish_values[i])

    for i, key in enumerate(gibberish_keys):
        ll_a.append((key, gibberish_values[i]))

    for i, key in enumerate(gibberish_keys):
        ll_b.append((key, gibberish_values[i]))

    return (hashtable, ll_a, ll_b)

def test_linked_list_comprehension(test_structures):
    actual = [node for node in test_structures[1]]
    ll_b = list(test_structures[2])
    expected = [
    ll_b[0], ll_b[1], ll_b[2], ll_b[3], ll_b[4], 
    ll_b[5], ll_b[6], ll_b[7], ll_b[8], ll_b[9], 
    ll_b[10], ll_b[11], ll_b[12], ll_b[13], ll_b[14], 
    ll_b[15], ll_b[16], ll_b[17], ll_b[18], ll_b[19]
    ]
    assert actual == expected

def test_linked_list_for_in(test_structures):
    actual = []
    for node in test_structures[1]:
        actual.append(node)
    ll_b = list(test_structures[2])
    expected = [
    ll_b[0], ll_b[1], ll_b[2], ll_b[3], ll_b[4], 
    ll_b[5], ll_b[6], ll_b[7], ll_b[8], ll_b[9], 
    ll_b[10], ll_b[11], ll_b[12], ll_b[13], ll_b[14], 
    ll_b[15], ll_b[16], ll_b[17], ll_b[18], ll_b[19]
    ]
    assert actual == expected

def test_linked_list_get_item(test_structures):
    actual = test_structures[1]
    expected = list(test_structures[2])
    assert actual[4] == expected[4]

def test_hashtable_str(test_structures):
    actual = str(test_structures[0])
    ll_a = list(test_structures[1])
    expected =(
      f'=========================\n'
      f'Bucket: 1008\n'
      f'=========================\n'
      f'Key:{ll_a[0][0]} | Value:{ll_a[0][1]}\n'
      f'Key:{ll_a[1][0]} | Value:{ll_a[1][1]}\n'
      f'Key:{ll_a[2][0]} | Value:{ll_a[2][1]}\n'
      f'Key:{ll_a[3][0]} | Value:{ll_a[3][1]}\n'
      f'Key:{ll_a[4][0]} | Value:{ll_a[4][1]}\n'
      f'Key:{ll_a[5][0]} | Value:{ll_a[5][1]}\n'
      f'Key:{ll_a[6][0]} | Value:{ll_a[6][1]}\n'
      f'Key:{ll_a[7][0]} | Value:{ll_a[7][1]}\n'
      f'Key:{ll_a[8][0]} | Value:{ll_a[8][1]}\n'
      f'Key:{ll_a[9][0]} | Value:{ll_a[9][1]}\n'
      f'Key:{ll_a[10][0]} | Value:{ll_a[10][1]}\n'
      f'Key:{ll_a[11][0]} | Value:{ll_a[11][1]}\n'
      f'Key:{ll_a[12][0]} | Value:{ll_a[12][1]}\n'
      f'Key:{ll_a[13][0]} | Value:{ll_a[13][1]}\n'
      f'Key:{ll_a[14][0]} | Value:{ll_a[14][1]}\n'
      f'Key:{ll_a[15][0]} | Value:{ll_a[15][1]}\n'
      f'Key:{ll_a[16][0]} | Value:{ll_a[16][1]}\n'
      f'Key:{ll_a[17][0]} | Value:{ll_a[17][1]}\n'
      f'Key:{ll_a[18][0]} | Value:{ll_a[18][1]}\n'
      f'Key:{ll_a[19][0]} | Value:{ll_a[19][1]}\n'
      f'None\n'
      f'=========================\n'
      f'20 line entries\n'
      f'=========================\n'
      f'\n'
      f'END OF LIST'
    )
    assert actual == expected

def test_linked_list_str(test_structures):
    actual = str(test_structures[2])
    ll_b = list(test_structures[2])
    expected =(
      f'Key:{ll_b[0][0]} | Value:{ll_b[0][1]}\n'
      f'Key:{ll_b[1][0]} | Value:{ll_b[1][1]}\n'
      f'Key:{ll_b[2][0]} | Value:{ll_b[2][1]}\n'
      f'Key:{ll_b[3][0]} | Value:{ll_b[3][1]}\n'
      f'Key:{ll_b[4][0]} | Value:{ll_b[4][1]}\n'
      f'Key:{ll_b[5][0]} | Value:{ll_b[5][1]}\n'
      f'Key:{ll_b[6][0]} | Value:{ll_b[6][1]}\n'
      f'Key:{ll_b[7][0]} | Value:{ll_b[7][1]}\n'
      f'Key:{ll_b[8][0]} | Value:{ll_b[8][1]}\n'
      f'Key:{ll_b[9][0]} | Value:{ll_b[9][1]}\n'
      f'Key:{ll_b[10][0]} | Value:{ll_b[10][1]}\n'
      f'Key:{ll_b[11][0]} | Value:{ll_b[11][1]}\n'
      f'Key:{ll_b[12][0]} | Value:{ll_b[12][1]}\n'
      f'Key:{ll_b[13][0]} | Value:{ll_b[13][1]}\n'
      f'Key:{ll_b[14][0]} | Value:{ll_b[14][1]}\n'
      f'Key:{ll_b[15][0]} | Value:{ll_b[15][1]}\n'
      f'Key:{ll_b[16][0]} | Value:{ll_b[16][1]}\n'
      f'Key:{ll_b[17][0]} | Value:{ll_b[17][1]}\n'
      f'Key:{ll_b[18][0]} | Value:{ll_b[18][1]}\n'
      f'Key:{ll_b[19][0]} | Value:{ll_b[19][1]}\n'
      f'None\n'
      f'=========================\n'
      f'20 line entries\n'
      f'========================='
    )

def test_linked_list_repr(test_structures):
    actual = repr(test_structures[1])
    expected = str(test_structures[1].head)

    assert actual == expected

def test_equal_info(test_structures):
    ll_a = list(test_structures[1])
    ll_b = list(test_structures[2])

    assert ll_a == ll_b

def test_entry_counter_decorator():
    @entry_counter
    def line_break_output(count):
        output = ''
        for i in range(count): output += f'{i+1}\n'
        return output

    actual = line_break_output(4)
    expected=(
      f'1\n'
      f'2\n'
      f'3\n'
      f'4\n'
      f'\n'
      f'=========================\n'
      f'4 line entries\n'
      f'=========================\n'
    )
    assert actual == expected

def test_gibberish_generator_hash_consistency(test_structures):
    key_list = []
    for node in test_structures[2]: key_list.append(node[0])
    actual = hash_consistency_check(key_list)
    expected = True
    assert actual == expected