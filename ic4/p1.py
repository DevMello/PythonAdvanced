def hash_function(key, table_size):
    return key % table_size

def insert_linear_probing(hash_table, key):
    table_size = len(hash_table)
    index = hash_function(key, table_size)
    
    
    if hash_table[index] is None:
        hash_table[index] = key
    else:
        
        while hash_table[index] is not None:
            index = (index + 1) % table_size
        hash_table[index] = key

def build_hash_table(keys, table_size):
    hash_table = [None] * table_size
    
    for key in keys:
        insert_linear_probing(hash_table, key)
    
    return hash_table


keys = [12, 18, 13, 2, 3, 23, 5, 15]

table_size = 10

resultant_hash_table = build_hash_table(keys, table_size)


print("Resultant Hash Table:")
print(resultant_hash_table)