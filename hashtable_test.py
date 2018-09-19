# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

for (name, HashTable) in [("chaining", HashTableChaining), ("linear probing", HashTableProbing)]:
    table = HashTable()
    table.insert("example_key", "example_value")
    print table.get("example_key")
    if table.get("example_key") != "example_value":
        print("%s hash table did not return example value"%name)
    table.remove("example_key")
    if table.size() != 0:
        print("%s hash table had non-zero size"%name)


# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.
from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing
for (name, HashTable) in [("linear probing", HashTableProbing), ("chaining", HashTableChaining)]:
    table = HashTable()
    print(table.array.items)
    table.insert("example_key", "example_value")
    print(table.array.items)
    table.insert("example_key", "example_value")
    print(table.array.items)
    assert(table.size() == 1)
    table.insert("example_key", "rewrite_value")
    print(table.array.items)
    assert(table.size() == 1)
    assert(table.get("example_key") == "rewrite_value")
    table.insert("example1", "rand1")
    print(table.array.items)
    table.insert("example2", "rand2")
    print(table.array.items)
    table.insert("example3", "rand3")
    print(table.array.items)
    table.insert("example4", "rand4")
    print(table.array.items)
    table.insert("example5", "rand5")
    print(table.array.items)
    table.insert("example6", "rand6")
    print(table.array.items)
    assert(table.array_size == 10)
    table.insert("example7", "rand7")
    print(table.array.items)
    table.insert("example8", "rand8")
    print(table.array.items)
    assert(table.array_size == 20)
    table.insert("example9", "rand9")
    print(table.array.items)
    assert(table.array_size == 20)
    table.insert("example10", "rand10")
    print(table.array.items)
    table.remove("example9")
    assert(table.get("example9") == None)
    assert(table.get("example10") == "rand10")
    table.remove("example2")
    assert(table.get("example10") == "rand10")
    assert(table.get("example2") == None)
    print(table.array.items)
    table.remove("example2")
    table.insert("example2", "rand22")
    assert(table.get("example10") == "rand10")
    assert(table.get("example2") == "rand22")
    print(table.array.items)
    table.remove("example2")
    table.remove("example2")
    table.remove("example2")
    table.remove("example2")
    table.remove("example2")
    if table.get("example_key") != "rewrite_value":
        print("%s hash table did not return example value"%name)
    table.remove("example_key")
    if table.size() != 8:
        print("%s hash table had non-zero size"%name)
