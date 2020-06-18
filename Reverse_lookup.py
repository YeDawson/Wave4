#Reverse Lookup
def reverseLookup(dictionary, target):
    keys_list = []
    for keys, value in dictionary.items():
        if value == target:
            keys_list.append(keys)
    return keys_list
# multiple keys
assert reverseLookup({"a": 1, "b": 1, "c": 1}, 1) == ['a', 'b', 'c']
# single key
assert reverseLookup({"a": 1, "b": 2, "c": 2}, 1) == ['a']
# no keys
assert reverseLookup({"a": 2, "b": 2, "c": 2}, 1) == []
