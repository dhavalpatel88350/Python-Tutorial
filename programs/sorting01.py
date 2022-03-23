
def take_second(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
sorted_list = sorted(random, key=take_second)
print('Sorted list:', sorted_list)
