#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    if len(weights) < 2:
        return None
    else:
        for index in weights:
          
            hash_table_insert(ht, index, index)

    count = 0
    answer = ()
    result = []

    for key in ht.storage:
        if key is None:
            continue
        elif key.next is None:
            index = key.key
            value = key.value
            print(index, "index")
            print(value, "stored value")
            
        else:
            current_key = key
            while True:
                index = current_key.key
                value = current_key.value
                print(index, "index")
                print(value, "stored value")
                if current_key.next is None:
                    break
                else:
                    current_key = current_key.next
    
    
    return answer   # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([2,2,3,4,5], 2, 4))