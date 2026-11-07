def func():
    return "Hello World"

def procedure():
    print("I'm just a procedure")

# print(func())
# res = procedure
# res()
# print(res)

def many_parameters(a, b="two", c="three"):
    print("a", a)
    print("b", b)
    print("c", c)
    return "Just Finished"

many_parameters("1", 2, "three")
many_parameters("other a", c="cee")

def ticket_category(price, low_tier=10, high_tier=50):
    if price < low_tier:
        return "cheap"
    if price < high_tier:
        return "medium"
    return "expensive"

res = ticket_category(5)
print("Ticket category:", res)

nums = [1, 2, 3, 4, 5, 9]
other_nums = [2, 10, 100, 1000, 1000, 2000, 500, 200]

def average(numbers):
    # remember to use correct variables
    # s = sum(nums)
    s = sum(numbers)
    return s/len(numbers)

print("Average: ", average(nums))
print("Average: ", average(other_nums))

def add_to_list(sequence, element):
    # remember to make a copy
    res = sequence[:]
    res.append(element)
    return res

l = [1, 2, 3]
big_list = add_to_list(l, 4)
print(big_list)
print(l)

def extend_list(element, sequence=None):
    if not sequence:
        sequence = []
    sequence.append(element)
    return sequence

big_list = extend_list(4)
print(big_list)
another_list = extend_list(5)
print(another_list)
another_list_2 = extend_list(6)
print(another_list_2)
another_list_3 = extend_list(6, l)
print(another_list_3)

