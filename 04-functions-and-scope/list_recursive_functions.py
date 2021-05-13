# appending a list of integers to another list of integers

def list_append_recursive(l1: list, l2: list):
    if len(l2) == 0:
        return l1
    else:
        l1.append(l2.pop(0))
        return list_append_recursive(l1, l2)

def list_append_loop(l1: list, l2: list):
    for i in l2:
        l1.append(i)
    return l1
    
print(list_append_recursive([1,2,3,4], [5,6,7,8]))
print(list_append_loop([1,2,3,4], [5,6,7,8]))
