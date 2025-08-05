
my_list = [10, 5, 8, 22, 13, 7]

print("Original list:", my_list)
print("First element (indexing):", my_list[0])
print("Last 3 elements (slicing):", my_list[-3:])


my_list.append(30)
my_list.remove(5)
my_list.sort()

print("Modified list (sorted, added 30, removed 5):", my_list)

squared = [x**2 for x in my_list if x % 2 == 0]
print("Squared even numbers using list comprehension:", squared)

my_tuple = (100, 200, 300)
print("Tuple:", my_tuple)
print("Tuple first element:", my_tuple[0])


def get_min_max(lst):
    return min(lst), max(lst)

min_val, max_val = get_min_max(my_list)
print("Min and Max from list (tuple unpacking):", min_val, max_val)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union of sets:", union_set)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2  
print("Merged dictionaries using |:", merged_dict)


descending = sorted(my_list, reverse=True)
print("List sorted in descending order:", descending)


filtered = [x for x in my_list if x > 10]
print("Filtered (values > 10):", filtered)

tuple_list = list(my_tuple)
doubled = [x * 2 for x in tuple_list]
new_tuple = tuple(doubled)
print("Transformed tuple (elements doubled):", new_tuple)


def find_second_largest(numbers):
    unique_numbers = list(set(numbers))  
    if len(unique_numbers) < 2:
        return None 
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

test_list = [5, 1, 9, 6, 9, 5]
second_largest = find_second_largest(test_list)
print("Second-largest number:", second_largest)


dict_a = {'x': 10, 'y': 20}
dict_b = {'y': 50, 'z': 30}
merged = dict_a | dict_b
print("Merged dictionary:", merged)
