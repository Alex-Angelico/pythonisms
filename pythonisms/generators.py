from random import randint as random

# given a hash target
# generate a word with a number of letters such that the average 
# of the hash target divided by that number will be between 65 and 122
# fill each letter in order
# if the last letter to be filled must have a prohibited ascii value below 65
# remove the first above-average letter in the string and attempt to fill the last two letters again
# if the last letter to be filled must have a prohibited ascii value above 122
# remove the first below-average letter in the string and attempt to fill the last two letters again
# if the last letter to be filled must have a prohibited ascii value between 91 and 96
# remove the letter nearest the average in the string and attempt to fill the last two letters again
# else, fill the last letter with the ascii value equivalent to the difference remaining between the sum limit and 0

def gibberish_generator(word_count=int, sum_target=0):
    i = 0
    if sum_target != 0 and sum_target < 200:
        raise ValueError(f'sum_target minimum value is 200; value provided was {sum_target}.')
    while i < word_count:
        ascii_limit, count = sum_target, 0
        if sum_target:
            ascii_average = random(81, 106)
            letter_count = sum_target // ascii_average
            if sum_target / letter_count > 122:
                while sum_target / letter_count > 122: letter_count += 1
            if sum_target / letter_count < 65:
                while sum_target / letter_count < 65: letter_count -= 1
        else: letter_count = random(3, 8)
        word = letter_count * [None]
        def letter_remover(boolean, index):
            nonlocal ascii_limit, count
            word_reference = word.copy()
            word_reference.pop(-1)
            word_reference.sort(reverse=boolean)
            if not len(word_reference) > 1: index -= 1
            word.remove(word_reference[index])
            word.append(None)
            ascii_limit, count = ascii_limit + ord(word_reference[index]), count - 1
        while count < letter_count:
            if sum_target != 0 and letter_count - count == 1:
                if ascii_limit < 65: letter_remover(True, 0)
                elif ascii_limit > 122: letter_remover(False, 0)
                elif ascii_limit in range(91, 97): letter_remover(False, len(word) // 2)
                else: word[count], count = chr(ascii_limit), count + 1
            else:
                ascii_value = (random(97, 122) if random(0, 1) else random(65, 90))
                ascii_limit, word[count], count = ascii_limit - ascii_value, chr(ascii_value), count + 1
        yield ''.join(word)
        i += 1

def hash_consistency_check(string_set):
    reference_sum = 0
    for string in string_set:
        current_sum = 0
        for character in string: current_sum += ord(character)
        if not reference_sum: reference_sum = current_sum
        if current_sum != reference_sum: return False
    return True