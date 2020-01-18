#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    count = 0
    result = []
    
    if length < 2:
        return None
    else:
       
        for idx, val in enumerate(weights):
            hash_table_insert(ht, val, idx)
            count += 1

    if count == length:
        for i in weights:
            
            check = limit - i
            print(i, "i")
            print(check, "check")
            index = hash_table_retrieve(ht, check)
            if index is not None:
                result.append(index)
                print(ht.storage[1])
   
    if len(result) == 2:
        if result[0] == result[1]:
            result[0] = 0

        
    answer_arr = sorted(result, reverse=True)
    answer = tuple(answer_arr) 
    return answer


    # def print_answer(answer):
    #     if answer is not None:
    #         print(str(answer[0]) + " " + str(answer[1]))
    #     else:
    #         print("None")
    
    # print_answer(answer)

test = get_indices_of_item_weights([4,4], 2, 8)
print(test)
# print(test[0])
# print(test[1])

# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
# print(answer_3)
# print(answer_3[0])
# print(answer_3[1])
    # self.assertTrue(answer_3[0] == 3)
    # self.assertTrue(answer_3[1] == 1)


# for key in ht.storage:
#         if key is None:
#             continue
#         elif key.next is None:
#             index = key.key
#             value = key.value
#             print(index, "index")
#             print(value, "stored value")
            
#         else:
#             current_key = key
#             while True:
#                 index = current_key.key
#                 value = current_key.value
#                 print(index, "index")
#                 print(value, "stored value")
#                 if current_key.next is None:
#                     break
#                 else:
#                     current_key = current_key.next
    
    