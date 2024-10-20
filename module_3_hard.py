def calculate_structure_sum(*args):
    count = 0
    #list_my = []
    for i in args:
        if isinstance(i, str):
            #list_my = list_my + list(i)   
            count += len(i)         
        if isinstance(i, int):
            #list_my.append(i)
            count += i
        if isinstance(i, (set, tuple, list)):
            #list_my = list_my + list(i)
            count += calculate_structure_sum(*i)
        if i == None:
            continue
        if isinstance(i, dict):
            #list_my = list_my + list(i.values()) + list(i.keys())
            count += calculate_structure_sum(*i.values())
            count += calculate_structure_sum(*i.keys())
    return count


data_structure = [
   [1, 2, 3],
   {'a': 4, 'b': 5},
   (6, {'cube': 7, 'drum': 8}),
   "Hello",
   ((), [{(2, 'Urban', ('Urban2', 35))}])
 ]

result = calculate_structure_sum(data_structure)
print(result)