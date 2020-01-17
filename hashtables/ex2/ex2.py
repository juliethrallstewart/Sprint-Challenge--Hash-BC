#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    count = 0

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    if len(hashtable.storage) == len(tickets):
        get_first_key = hash_table_retrieve(hashtable, "NONE")
        current_key = get_first_key
        for i in tickets:
            print(f"source {i.source}, destination: {i.destination}")
            if count == 0:
                route[count] = get_first_key
                count += 1
            else:
                get_route = hash_table_retrieve(hashtable, current_key)
                route[count] = get_route
                current_key = get_route
                count += 1
    
    return route
        
 

   



# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]
# print(reconstruct_trip(tickets, 3), "this is the route")

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
            "SLC", "PIT", "ORD", "NONE"]
result = reconstruct_trip(tickets, 10)
print(result, "this is the route")

# def reconstruct_trip(tickets, length):
#     hashtable = HashTable(length)
#     route = [None] * length
#     count = 0

#     prev_destination = [0]
#     # print(prev_destination, "prev destination")
#     for i in tickets:
#         print(i.source, "line 23")
#         if i.source == "NONE":
#             print(i.source, "line 25")
#             hash_table_insert(hashtable, i.source,i.destination)
#             prev_destination[0] = i.destination
#             print(prev_destination, "line 27")
#             route[count] = prev_destination[0]
#             count += 1
#             print(count, "count")
#             continue
  
#         elif i.source == prev_destination[0]:
#             print(i.source, "i source")
#             print(prev_destination, "prev dest")
#             hash_table_insert(hashtable, i.source, i.destination)
#             prev_destination[0] = i.destination
#             route[count] = prev_destination[0]
#             count += 1
#             continue
    
#     return route